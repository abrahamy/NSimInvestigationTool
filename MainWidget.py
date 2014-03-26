__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

from PyQt5 import QtCore, QtWidgets

from ui_MainWidget import Ui_MainWidget
from SearchForm import SearchForm


class MainWidget(QtWidgets.QTabWidget, Ui_MainWidget):

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

    @QtCore.pyqtSlot()
    def on_btnInfoSearch_clicked(self):
        pass

    @QtCore.pyqtSlot()
    def on_btnDbSearch_click(self):
        pass