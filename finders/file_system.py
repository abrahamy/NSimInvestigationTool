__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import os
import zipfile
import logging

from PyQt5 import QtCore

from .signals import SignalFactory


class FileSystemFinder(QtCore.QRunnable):

    def __init__(self, task):
        super(FileSystemFinder, self).__init__()

        self.folders = task.folders
        self.mobile_numbers = task.mobile_numbers
        self.signals = SignalFactory()

        self.logger = logging.getLogger(__name__)

    def check_exists(self, haystack):
        for needle in self.mobile_numbers:
            try:
                haystack.index(needle)
                return True
            except ValueError:
                continue

        return False

    @classmethod
    def get_zip_files(cls, folders):
        zip_files = []
        for folder in folders:
            for (dirpath, dirnames, filenames) in os.walk(folder):
                filtered = filter(lambda filename: filename.lower().endswith('.zip'), filenames)
                zip_files.extend([os.path.join(dirpath, filename) for filename in filtered])

        return zip_files

    def run(self):
        self.logger.info('New search started in %s' % repr(self.folders))
        zfiles = self.__class__.get_zip_files(self.folders)
        total_count = len(zfiles)
        current_count = 0
        num_found = 0

        for zfile in zfiles:
            current_count += 1
            self.signals.statusChanged.emit(current_count, total_count)
            self.logger.info('Processing %s of %s packets' % (current_count, total_count))
            try:
                with zipfile.ZipFile(zfile) as packet:
                    self.logger.info('Current packet: %s' % zfile)
                    xmls = [i for i in packet.namelist() if i.lower().endswith('.xml')]

                    for xmlfile in xmls:
                        haystack = packet.open(xmlfile).read().decode()

                        if self.check_exists(haystack):
                            num_found += 1
                            msg = 'Found match in [%s] from [%s]. Total matches so far: %s' % (zfile, xmlfile, num_found)
                            self.signals.itemFound.emit(zfile, xmlfile)
                            self.logger.info(msg)

            except Exception as e:
                self.logger.error('Encountered and error while processing [%s]. Error Message: [%s]' % (zfile, repr(e)))

        self.logger.info('Search completed in %s' % self.folders)
        self.signals.completed.emit()
