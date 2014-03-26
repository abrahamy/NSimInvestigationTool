__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

from PyQt5 import QtCore, QtWidgets

from ui_SearchForm import Ui_SearchForm


class SearchForm(QtWidgets.QWidget, Ui_SearchForm):

    def __init__(self, parent=None):
        super(SearchForm, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.lblStatus.setText('')

    @QtCore.pyqtSlot()
    def on_btnGetFile_clicked(self):
        pass

    @QtCore.pyqtSlot()
    def on_btnSearch_clicked(self):
        pass

    @QtCore.pyqtSlot()
    def on_tblResult_itemClicked(self, item):
        pass