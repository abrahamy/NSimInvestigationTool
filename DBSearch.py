__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import logging

from PyQt5 import QtCore, QtWidgets, QtGui

from ui_DBSearch import Ui_DBSearch
from finders import DatabaseFinder
from finders.tasks import FindInDb, clean


class DBSearch(QtWidgets.QWidget, Ui_DBSearch):

    def __init__(self, parent=None):
        super(DBSearch, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.lblStatus.setText('')
        self.btnSaveAs.setEnabled(False)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timeout)

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

        self.txtResult.setPlainText('')
        self.btnSaveAs.setEnabled(False)

        self.startSearch()

    def startSearch(self):
        task = FindInDb(self.txtMobileNos.toPlainText().strip())
        self.finder = DatabaseFinder(task)

        self.finder.signals.completedWithResult.connect(self.on_search_completed)
        self.finder.signals.onError.connect(self.on_error)

        self.lblStatus.setText('Loading')
        self.btnSearch.setEnabled(False)
        self.setCursor(QtCore.Qt.BusyCursor)

        self.timer.start(500)
        self.thread_pool.start(self.finder)

    @QtCore.pyqtSlot(tuple)
    def on_search_completed(self, rows):
        self.reset_ui()

        text = 'Mobile Number\tPacket\tXML Filename\n%s' % '\n'.join(['\t'.join(row) for row in rows])
        self.txtResult.setPlainText(text)
        
        if self.txtResult.toPlainText().strip():
            self.btnSaveAs.setEnabled(True)

        QtWidgets.QMessageBox.information(self, 'Info', 'Search Completed!')
        
    @QtCore.pyqtSlot(str)
    def on_error(self, error_msg):
        self.reset_ui()
        
        QtWidgets.QMessageBox.critical(self, 'Error', error_msg)
        
    def reset_ui(self):
        self.timer.stop()
        self.btnSearch.setEnabled(True)

        self.lblStatus.setText('')
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.finder = None

    @QtCore.pyqtSlot()
    def on_btnSaveAs_clicked(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', QtCore.QDir.homePath(), 'Text Files (*.txt *.rtf)')[0]
        if file_name:
            try:
                with open(file_name, 'w') as dest:
                    dest.write(self.txtResult.toPlainText())

                QtWidgets.QMessageBox.information(self, 'Info', 'Result saved!')

            except Exception as e:
                self.logger.error(repr(e))
                message = ('Unable to write file. Please ensure that the ',
                           'current user has write access to the selected file.').join('')
                QtWidgets.QMessageBox.critical(self, 'Error', message)

    @QtCore.pyqtSlot()
    def on_timeout(self):
        if self.lblStatus.text() == 'Loading':
            self.lblStatus.setText('Loading.')
        elif self.lblStatus.text() == 'Loading.':
            self.lblStatus.setText('Loading..')
        elif self.lblStatus.text() == 'Loading..':
            self.lblStatus.setText('Loading...')
        else:
            self.lblStatus.setText('Loading')