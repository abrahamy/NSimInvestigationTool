__author__ = 'Administrator'

from PyQt5 import QtCore, QtWidgets

from ui_SearchDlg import Ui_SearchDlg
from viewerDlg import ViewerDlg
from finders import MobileNumberFinder, MobileNumberFinderTask
from datastructures import FEPRecord


class SearchDlg(QtWidgets.QDialog, Ui_SearchDlg):

    def __init__(self, parent=None):
        super(SearchDlg, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.progressBar.setVisible(False)

        self.searchPath = None

    @QtCore.pyqtSlot('QString')
    def on_txtMobileNo_textChanged(self, text):
        try:
            int(text[-1])
        except:
            self.txtMobileNo.setText(text[:-1])

    @QtCore.pyqtSlot()
    def on_btnFolder_clicked(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.lblFolder.setText(folder)

        self.searchPath = folder

    @QtCore.pyqtSlot()
    def on_btnSearch_clicked(self):
        if self.txtMobileNo.text().strip() == '':
            QtWidgets.QMessageBox.information(self, 'Info', 'You have not entered a mobile number.')
            return

        if self.lblFolder.text().strip() == '':
            QtWidgets.QMessageBox.information(self, 'Info', 'You have not selected an FEP/MNO folder.')
            return

        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)

        if hasattr(self, 'finder'):
            try:
                self.finder.signals.notifyProgress.disconnect(self.updateProgress)
                self.finder.signals.itemFound.disconnect(self.updateFoundList)
                self.finder.signals.finished.disconnect(self.on_search_finished)
            except:
                pass

        self.startSearch()

    def startSearch(self):
        task = MobileNumberFinderTask(self.txtMobileNo.text().strip(), self.searchPath)
        self.finder = MobileNumberFinder(task)
        self.finder.setAutoDelete(False)

        self.finder.signals.notifyProgress.connect(self.updateProgress)
        self.finder.signals.itemFound.connect(self.updateFoundList)
        self.finder.signals.finished.connect(self.on_search_finished)

        self.progressBar.setVisible(True)
        self.setCursor(QtCore.Qt.BusyCursor)

        QtCore.QThreadPool.globalInstance().start(self.finder)

    @QtCore.pyqtSlot(int)
    def updateProgress(self, pos):
        self.progressBar.setValue(pos)

    @QtCore.pyqtSlot(str, str)
    def updateFoundList(self, packet, xmlfilename):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(packet))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(xmlfilename))

    @QtCore.pyqtSlot()
    def on_search_finished(self):
        self.progressBar.setVisible(False)
        self.progressBar.setValue(0)
        self.setCursor(QtCore.Qt.ArrowCursor)
        QtWidgets.QMessageBox.information(self, 'Search completed!', 'Found %s matches.' % self.tableWidget.rowCount())

        del self.finder

    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)
    def on_tableWidget_itemClicked(self, item):
        packet = self.tableWidget.item(item.row(), 0).text()
        xmlfile = self.tableWidget.item(item.row(), 1).text()
        dialog = ViewerDlg(parent=self, item=FEPRecord(packet, xmlfile))
        dialog.setModal(True)
        dialog.show()
        #dialog.exec()
