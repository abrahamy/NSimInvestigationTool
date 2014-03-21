__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import sys
from PyQt5 import QtWidgets

from searchDlg import SearchDlg


class NSimApplication(QtWidgets.QApplication):

    def __init__(self):
        super(NSimApplication, self).__init__(sys.argv)

        self.setOrganizationName('SW Global Limited')
        self.setApplicationName('NSim Investigation Tool')

        window = SearchDlg()
        window.show()

        self.exec_()

if __name__ == '__main__':
    NSimApplication()
