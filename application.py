__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import sys
import logging

from PyQt5 import QtWidgets

from MainWidget import MainWidget


class NSimApplication(QtWidgets.QApplication):

    def __init__(self):
        super(NSimApplication, self).__init__(sys.argv)

        self.setOrganizationName('SW Global Limited')
        self.setApplicationName('NSim Investigation Tool')

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)-8s %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S',
            filename='logs/log.txt',
            filemode='w'
        )

        window = MainWidget()
        window.show()

        self.exec_()


if __name__ == '__main__':
    NSimApplication()
