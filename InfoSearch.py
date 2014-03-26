__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

from PyQt5 import QtCore, QtWidgets

from ui_InfoSearch import Ui_InfoSearch
from finders.tasks import FindInFolder, clean


class InfoSearch(QtWidgets.QWidget, Ui_InfoSearch):

    def __init__(self, parent=None):
        super(InfoSearch, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

    @QtCore.pyqtSlot()
    def on_btnGetFolder_clicked(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.lblFolder.setText(folder)

    @QtCore.pyqtSlot()
    def on_btnGetFile_clicked(self):
        pass

    @QtCore.pyqtSlot()
    def on_btnSearch_clicked(self):
        pass

    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)
    def on_tblResult_itemClicked(self, item):
        packet = self.tblResult.item(item.row(), 0).text()
        xmlfile = self.tblResult.item(item.row(), 1).text()
        dialog = ViewerDlg(parent=self, item=FEPRecord(packet, xmlfile))
        dialog.setModal(True)
        dialog.show()