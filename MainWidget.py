__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

from PyQt5 import QtCore, QtWidgets

from ui_MainWidget import Ui_MainWidget
from DBSearch import DBSearch
from InfoSearch import InfoSearch


class MainWidget(QtWidgets.QTabWidget, Ui_MainWidget):

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

    @QtCore.pyqtSlot()
    def on_btnInfoSearch_clicked(self):
        self.insertTab(InfoSearch(), 1)

    @QtCore.pyqtSlot()
    def on_btnDbSearch_click(self):
        self.insertTab(DBSearch(), 1)