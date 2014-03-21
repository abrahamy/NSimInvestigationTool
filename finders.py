__author__ = 'Administrator'

import os
import zipfile

from PyQt5 import QtCore

from datastructures import FEPRecord

class MobileNumberFinder(QtCore.QRunnable):

    def __init__(self, task=None):
        super(MobileNumberFinder, self).__init__()

        self.task = task
        self.signals = FinderSignals()

    def run(self):
        zfiles = [os.path.join(self.task.folder, i) for i in os.listdir(self.task.folder) if i.lower().endswith('.zip')]
        totalCount = len(zfiles)
        currentCount = 0
        numFound = 0

        for zfile in zfiles:
            currentCount += 1
            self.signals.notifyProgress.emit(currentCount, totalCount)
            self.signals.message.emit('Processing %s of %s packets' % (currentCount, totalCount))
            try:
                with zipfile.ZipFile(zfile) as packet:
                    self.signals.message.emit('Current packet: [%s]' % zfile)
                    xmls = [i for i in packet.namelist() if i.lower().endswith('.xml')]

                    for xmlfile in xmls:
                        needle = self.task.mobileno.strip()
                        haystack = packet.open(xmlfile).read().decode()

                        if haystack.find(needle) is not -1:
                            numFound += 1
                            msg = 'Found match in [%s] from [%s]. Total matches so far: %s' % (zfile, xmlfile, numFound)
                            self.signals.itemFound.emit(zfile, xmlfile)
                            self.signals.message.emit(msg)

            except Exception as e:
                self.signals.message.emit(repr(e))

        self.signals.message.emit('Search completed for %s in %s' % (self.task.mobileno, self.task.folder))
        self.signals.finished.emit()

class FinderSignals(QtCore.QObject):
    notifyProgress = QtCore.pyqtSignal(int, int)
    finished = QtCore.pyqtSignal()
    itemFound = QtCore.pyqtSignal(str, str, name='itemFound')  # arg1: packetName, arg2: xmlFileName
    message = QtCore.pyqtSignal(str)


class MobileNumberFinderTask(object):

    def __init__(self, mobileno, folder):
        self.mobileno = mobileno
        self.folder = folder