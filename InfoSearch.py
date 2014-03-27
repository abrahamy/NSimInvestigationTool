__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import logging

from PyQt5 import QtCore, QtWidgets, QtGui

from datastructures import FEPRecord
from finders import FileSystemFinder
from finders.tasks import FindInFolder, clean

from ui_InfoSearch import Ui_InfoSearch
from SubscriberInfo import SubscriberInfo


class InfoSearch(QtWidgets.QWidget, Ui_InfoSearch):

    def __init__(self, parent=None):
        super(InfoSearch, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.lblFolder.setText('')
        self.lblStatus.setText('')

        self.thread_pool = QtCore.QThreadPool(self)
        self.thread_pool.setMaxThreadCount(1)

        self.finder = None

        self.logger = logging.getLogger(__name__)

    @QtCore.pyqtSlot()
    def on_txtMobileNos_textChanged(self):
        text = self.txtMobileNos.toPlainText()
        if text[-1] not in '0123456789,':
            self.txtMobileNos.setPlainText(text[:-1])
            cursor = self.txtMobileNos.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            self.txtMobileNos.setTextCursor(cursor)

    @QtCore.pyqtSlot()
    def on_btnGetFolder_clicked(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'FEP/MNO Folder', QtCore.QDir.homePath())
        if folder:
            self.lblFolder.setText(folder)

    @QtCore.pyqtSlot()
    def on_btnGetFile_clicked(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.homePath(), 'Text Files (*.txt *.rtf)')[0]
        if file_name:
            try:
                with open(file_name) as source:
                    mobile_nos = source.read().split(',')

                    self.txtMobileNos.setText(','.join(clean(mobile_nos)))

            except Exception as e:
                self.logger.error(repr(e))
                QtWidgets.QMessageBox.critical(self, 'Error', 'Unable to read from selected file.')

    @QtCore.pyqtSlot()
    def on_btnSearch_clicked(self):
        if self.txtMobileNos.toPlainText().strip() == '':
            QtWidgets.QMessageBox.information(self, 'Info', 'You have not entered a mobile number.')
            return

        if self.lblFolder.text().strip() == '':
            QtWidgets.QMessageBox.information(self, 'Info', 'You have not selected an FEP/MNO folder.')
            return

        self.tblResult.clearContents()

        self.tblResult.setHorizontalHeaderLabels(['Packet', 'XML File'])

        self.startSearch()

    def startSearch(self):
        task = FindInFolder(self.txtMobileNos.toPlainText().strip(), self.lblFolder.text())
        self.finder = FileSystemFinder(task)

        self.finder.signals.itemFound.connect(self.on_finder_foundItem)
        self.finder.signals.statusChanged.connect(self.on_finder_statusChanged)
        self.finder.signals.completed.connect(self.on_search_completed)

        self.lblStatus.setText('')
        self.btnSearch.setEnabled(False)
        self.setCursor(QtCore.Qt.BusyCursor)

        self.thread_pool.start(self.finder)

    @QtCore.pyqtSlot(str, str)
    def on_finder_foundItem(self, packet, xmlfilename):
        row = self.tblResult.rowCount()
        self.tblResult.insertRow(row)
        self.tblResult.setItem(row, 0, QtWidgets.QTableWidgetItem(packet))
        self.tblResult.setItem(row, 1, QtWidgets.QTableWidgetItem(xmlfilename))

    @QtCore.pyqtSlot(int, int)
    def on_finder_statusChanged(self, currentCount, totalCount):
        self.lblStatus.setText('Processing %s of %s packets' % (currentCount, totalCount))

    @QtCore.pyqtSlot()
    def on_search_completed(self):
        self.lblStatus.setText('')
        self.btnSearch.setEnabled(True)
        self.setCursor(QtCore.Qt.ArrowCursor)
        QtWidgets.QMessageBox.information(self, 'Search completed!', 'Found %s matches.' % self.tblResult.rowCount())

        self.finder = None

    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)
    def on_tblResult_itemClicked(self, item):
        packet = self.tblResult.item(item.row(), 0).text()
        xmlfile = self.tblResult.item(item.row(), 1).text()
        #dialog = ViewerDlg(parent=self, item=FEPRecord(packet, xmlfile))
        # dialog.setModal(True)
        # dialog.show()
