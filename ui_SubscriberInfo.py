# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubscriberInfo.ui'
#
# Created: Wed Mar 26 17:45:30 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SubscriberInfo(object):
    def setupUi(self, SubscriberInfo):
        SubscriberInfo.setObjectName("SubscriberInfo")
        SubscriberInfo.setWindowModality(QtCore.Qt.ApplicationModal)
        SubscriberInfo.resize(583, 438)
        SubscriberInfo.setSizeGripEnabled(False)
        SubscriberInfo.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SubscriberInfo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(SubscriberInfo)
        self.textBrowser.setTabChangesFocus(True)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnPrint = QtWidgets.QPushButton(SubscriberInfo)
        self.btnPrint.setObjectName("btnPrint")
        self.horizontalLayout.addWidget(self.btnPrint)
        self.btnClose = QtWidgets.QPushButton(SubscriberInfo)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SubscriberInfo)
        self.btnClose.clicked.connect(SubscriberInfo.reject)
        self.btnPrint.clicked.connect(SubscriberInfo.accept)
        QtCore.QMetaObject.connectSlotsByName(SubscriberInfo)
        SubscriberInfo.setTabOrder(self.textBrowser, self.btnPrint)
        SubscriberInfo.setTabOrder(self.btnPrint, self.btnClose)

    def retranslateUi(self, SubscriberInfo):
        _translate = QtCore.QCoreApplication.translate
        SubscriberInfo.setWindowTitle(_translate("SubscriberInfo", "Subscriber Information"))
        self.btnPrint.setText(_translate("SubscriberInfo", "&Print"))
        self.btnClose.setText(_translate("SubscriberInfo", "&Close"))

