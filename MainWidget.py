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
    def on_btnFileSystemSearch_clicked(self):
        self.insert_new_tab(InfoSearch(self), 'Retrieve Subscriber Information')

    @QtCore.pyqtSlot()
    def on_btnDbSearch_clicked(self):
        self.insert_new_tab(DBSearch(self), 'Find Packet Names')

    def insert_new_tab(self, widget, tab_text):
        for tab_index in range(self.count()):
            if self.tabText(tab_index) == tab_text:
                self.setCurrentIndex(tab_index)
                return

        new_tab_index = self.count()
        self.insertTab(new_tab_index, widget, tab_text)
        self.setTabEnabled(new_tab_index, True)
        self.setCurrentIndex(new_tab_index)