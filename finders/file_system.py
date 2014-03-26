__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import os
import zipfile

from PyQt5 import QtCore

from .signals import SignalFactory


class FileSystemFinder(QtCore.QRunnable):

    def __init__(self, task):
        super(FileSystemFinder, self).__init__()

        self.folder = task.folder
        self.mobile_numbers = task.mobile_numbers
        self.signals = SignalFactory()

    def check_exists(self, haystack):
        for needle in self.mobile_numbers:
            try:
                haystack.index(needle)
                return True
            except ValueError:
                continue

        return False

    def run(self):
        self.signals.info.emit('New search started in %s' % self.folder)
        zfiles = [os.path.join(self.folder, i) for i in os.listdir(self.folder) if i.lower().endswith('.zip')]
        total_count = len(zfiles)
        current_count = 0
        num_found = 0

        for zfile in zfiles:
            current_count += 1
            self.signals.statusChanged.emit(current_count, total_count)
            self.signals.info.emit('Processing %s of %s packets' % (current_count, total_count))
            try:
                with zipfile.ZipFile(zfile) as packet:
                    self.signals.info.emit('Current packet: %s' % zfile)
                    xmls = [i for i in packet.namelist() if i.lower().endswith('.xml')]

                    for xmlfile in xmls:
                        haystack = packet.open(xmlfile).read().decode()

                        if self.check_exists(haystack):
                            num_found += 1
                            msg = 'Found match in [%s] from [%s]. Total matches so far: %s' % (zfile, xmlfile, num_found)
                            self.signals.itemFound.emit(zfile, xmlfile)
                            self.signals.info.emit(msg)

            except Exception as e:
                self.signals.info.emit('Encountered and error while processing [%s]. Error Message: [%s]' % (zfile, repr(e)))

        self.signals.info.emit('Search completed in %s' % self.folder)
        self.signals.completed.emit()
