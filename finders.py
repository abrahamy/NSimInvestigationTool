__author__ = 'Administrator'

import os
import sys
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

        for zfile in zfiles:
            try:
                with zipfile.ZipFile(zfile) as packet:
                    xmls = [i for i in packet.namelist() if i.lower().endswith('.xml')]

                    for xmlfile in xmls:
                        needle = self.task.mobileno.strip()
                        haystack = packet.open(xmlfile).read().decode()

                        if haystack.find(needle) is not -1:
                            self.signals.itemFound.emit(zfile, xmlfile)

            except Exception as e:
                sys.stderr.write(repr(e))
                raise

            currentCount += 1
            progress = (float(currentCount) / totalCount) * 100
            self.signals.notifyProgress.emit(int(progress))

        self.signals.finished.emit()

class FinderSignals(QtCore.QObject):
    notifyProgress = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal()
    itemFound = QtCore.pyqtSignal(str, str, name='itemFound')  # arg1: packetName, arg2: xmlFileName


class MobileNumberFinderTask(object):

    def __init__(self, mobileno, folder):
        self.mobileno = mobileno
        self.folder = folder