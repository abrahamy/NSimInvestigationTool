__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import os

from PyQt5 import QtCore, QtWidgets

from ui_SubscriberInfo import Ui_SubscriberInfo


class SubscriberInfo(QtWidgets.QDialog, Ui_SubscriberInfo):

    def __init__(self, url, parent=None):
        super(SubscriberInfo, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.textBrowser.setSearchPaths([QtCore.QDir.tempPath()])
        self.textBrowser.setSource(QtCore.QUrl(url))

    @QtCore.pyqtSlot()
    def on_btnPrint_clicked(self):
        # print textbrowser content
        self.accept()