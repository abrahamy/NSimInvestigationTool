__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import os
import zipfile

from PyQt5 import QtCore

from datastructures import FEPRecord

class MobileNumberFinder(QtCore.QRunnable):

    def __init__(self, task=None):
        super(MobileNumberFinder, self).__init__()

        self.task = task
        self.signals = FinderSignals()
        self._mobileno_list = self.__class__.get_mobileno_list(self.task.mobileno)

    @classmethod
    def get_mobileno_list(cls, str_mobileno):
        mobileno_list = []
        for mobileno in [i.strip() for i in str_mobileno.split(',')]:
            mobileno_list.append(mobileno)
            if not mobileno.startswith('0'):
                mobileno_list.append('0%s' % mobileno)
            else:
                mobileno_list.append(mobileno[1:])

        return mobileno_list

    def check_exists(self, haystack):
        for needle in self._mobileno_list:
            try:
                haystack.index(needle)
                return True
            except ValueError:
                continue

        return False

    def run(self):
        self.signals.message.emit('Search started for %s in %s' % (self.task.mobileno, self.task.folder))
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
                        haystack = packet.open(xmlfile).read().decode()

                        if self.check_exists(haystack):
                            numFound += 1
                            msg = 'Found match in [%s] from [%s]. Total matches so far: %s' % (zfile, xmlfile, numFound)
                            self.signals.itemFound.emit(zfile, xmlfile)
                            self.signals.message.emit(msg)

            except Exception as e:
                self.signals.message.emit('Encountered and error while processing [%s]. Error Message: [%s]' % (zfile, repr(e)))

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
