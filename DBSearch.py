__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import logging

from PyQt5 import QtCore, QtWidgets

from ui_SearchForm import Ui_SearchForm
from finders import DatabaseFinder
from finders.tasks import FindInDb, clean


class DBSearch(QtWidgets.QWidget, Ui_SearchForm):

    def __init__(self, parent=None):
        super(DBSearch, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.lblStatus.setText('')
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timeout)

        self.thread_pool = QtCore.QThreadPool(self)
        self.thread_pool.setMaxThreadCount(1)

        self.finder = None

        self.logger = logging.getLogger(__path__)

    @QtCore.pyqtSlot()
    def on_btnGetFile_clicked(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName('Open File', QtCore.QDir.homePath(), 'Text Files (*.txt *.rtf)')
        try:
            with open(file_name) as source:
                mobile_nos = source.read().split(',')

                self.txtMobileNos.setText(clean(mobile_nos).join(','))

        except Exception as e:
            self.logger.error(repr(e))
            QtWidgets.QMessageBox.critical('Error', 'Unable to read from selected file.')

    @QtCore.pyqtSlot(str)
    def on_txtMobileNos_textChanged(self, text):
        if text[-1] not in '0123456789,':
            self.txtMobileNos.setText(text[:-1])

    @QtCore.pyqtSlot()
    def on_btnSearch_clicked(self):
        if self.txtMobileNos.text().strip() == '':
            QtWidgets.QMessageBox.information(self, 'Info', 'You have not entered a mobile number.')
            return

        if self.lblFolder.text().strip() == '':
            QtWidgets.QMessageBox.information(self, 'Info', 'You have not selected an FEP/MNO folder.')
            return

        self.txtResult.setPlainText('')

        del self.finder
        self.finder = None

        self.startSearch()

    def startSearch(self):
        task = FindInDb(self.txtMobileNo.text().strip())
        self.finder = DatabaseFinder(task)

        self.finder.signals.completedWithResult.connect(self.on_search_completed)

        self.lblStatus.setText('Loading')
        self.btnSearch.setEnabled(False)
        self.setCursor(QtCore.Qt.BusyCursor)

        self.timer.start(500)
        self.thread_pool.start(self.finder)

    @QtCore.pyqtSlot(tuple)
    def on_search_completed(self, rows):
        self.timer.stop()
        self.btnSearch.setEnabled(True)
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.finder = None

        text = 'Mobile Number\tPacket\tXML Filename\n%s' % [row.join('\t') for row in rows].join('\n')
        self.txtResult.setPlainText(text)

        QtWidgets.QMessageBox.information(self, 'Info', 'Search Completed!')

    @QtCore.pyqtSlot()
    def on_btnSaveAs_clicked(self, item):
        file_name = QtWidgets.QFileDialog.getSaveFileName('Save File', QtCore.QDir.homePath(), 'Text Files (*.txt *.rtf)')
        try:
            with open(file_name, 'w') as dest:
                dest.write(self.txtResult.text())

            QtWidgets.QMessageBox.information(self, 'Info', 'Result saved!')

        except Exception as e:
            self.logger.error(repr(e))
            message = 'Unable to write file. Please ensure that the current user has write access to the selected file.'
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