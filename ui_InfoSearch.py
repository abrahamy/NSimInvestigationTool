# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoSearch.ui'
#
# Created: Thu Mar 27 11:08:38 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InfoSearch(object):
    def setupUi(self, InfoSearch):
        InfoSearch.setObjectName("InfoSearch")
        InfoSearch.resize(640, 480)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(InfoSearch)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblMessage = QtWidgets.QLabel(InfoSearch)
        self.lblMessage.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: italic 10pt \"Segoe UI\";")
        self.lblMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout_3.addWidget(self.lblMessage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnGetFolder = QtWidgets.QPushButton(InfoSearch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGetFolder.sizePolicy().hasHeightForWidth())
        self.btnGetFolder.setSizePolicy(sizePolicy)
        self.btnGetFolder.setStyleSheet("color: rgb(5, 17, 127);\n"
"text-decoration: underline;\n"
"font: 10pt \"Segoe UI\";")
        self.btnGetFolder.setFlat(True)
        self.btnGetFolder.setObjectName("btnGetFolder")
        self.horizontalLayout_2.addWidget(self.btnGetFolder)
        self.lblFolder = QtWidgets.QLabel(InfoSearch)
        self.lblFolder.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: italic 10pt \"Segoe UI\";")
        self.lblFolder.setObjectName("lblFolder")
        self.horizontalLayout_2.addWidget(self.lblFolder)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lblMobileNos = QtWidgets.QLabel(InfoSearch)
        self.lblMobileNos.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        self.lblMobileNos.setObjectName("lblMobileNos")
        self.verticalLayout.addWidget(self.lblMobileNos)
        self.txtMobileNos = QtWidgets.QTextEdit(InfoSearch)
        self.txtMobileNos.setObjectName("txtMobileNos")
        self.verticalLayout.addWidget(self.txtMobileNos)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGetFile = QtWidgets.QPushButton(InfoSearch)
        self.btnGetFile.setStyleSheet("color: rgb(5, 17, 127);\n"
"text-decoration: underline;\n"
"font: 10pt \"Segoe UI\";")
        self.btnGetFile.setFlat(True)
        self.btnGetFile.setObjectName("btnGetFile")
        self.horizontalLayout.addWidget(self.btnGetFile)
        self.btnSearch = QtWidgets.QPushButton(InfoSearch)
        self.btnSearch.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.lblStatus = QtWidgets.QLabel(InfoSearch)
        self.lblStatus.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: italic 10pt \"Segoe UI\";")
        self.lblStatus.setScaledContents(False)
        self.lblStatus.setObjectName("lblStatus")
        self.horizontalLayout.addWidget(self.lblStatus)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblResult = QtWidgets.QLabel(InfoSearch)
        self.lblResult.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        self.lblResult.setObjectName("lblResult")
        self.verticalLayout_2.addWidget(self.lblResult)
        self.tblResult = QtWidgets.QTableWidget(InfoSearch)
        self.tblResult.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblResult.setTabKeyNavigation(False)
        self.tblResult.setAlternatingRowColors(True)
        self.tblResult.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblResult.setColumnCount(2)
        self.tblResult.setObjectName("tblResult")
        self.tblResult.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblResult.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblResult.setHorizontalHeaderItem(1, item)
        self.tblResult.horizontalHeader().setVisible(True)
        self.tblResult.horizontalHeader().setCascadingSectionResizes(True)
        self.tblResult.horizontalHeader().setDefaultSectionSize(300)
        self.tblResult.horizontalHeader().setMinimumSectionSize(1)
        self.tblResult.horizontalHeader().setSortIndicatorShown(False)
        self.tblResult.verticalHeader().setMinimumSectionSize(0)
        self.verticalLayout_2.addWidget(self.tblResult)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(InfoSearch)
        QtCore.QMetaObject.connectSlotsByName(InfoSearch)
        InfoSearch.setTabOrder(self.txtMobileNos, self.btnGetFile)
        InfoSearch.setTabOrder(self.btnGetFile, self.btnSearch)

    def retranslateUi(self, InfoSearch):
        _translate = QtCore.QCoreApplication.translate
        InfoSearch.setWindowTitle(_translate("InfoSearch", "Retrieve Subscriber Information"))
        self.lblMessage.setText(_translate("InfoSearch", "Enter a comma separated list of mobile numbers in the textbox below or click on \"Import From File\" to import from a text file."))
        self.btnGetFolder.setText(_translate("InfoSearch", "Click Here To Select FEP/MNO Folder"))
        self.lblFolder.setText(_translate("InfoSearch", "TextLabel"))
        self.lblMobileNos.setText(_translate("InfoSearch", "Mobile Numbers:"))
        self.btnGetFile.setText(_translate("InfoSearch", "Import From File"))
        self.btnSearch.setText(_translate("InfoSearch", "Search"))
        self.lblStatus.setText(_translate("InfoSearch", "Loading"))
        self.lblResult.setText(_translate("InfoSearch", "List of Items Found:"))
        self.tblResult.setToolTip(_translate("InfoSearch", "Click on a row to view subscriber information"))
        item = self.tblResult.horizontalHeaderItem(0)
        item.setText(_translate("InfoSearch", "Packet"))
        item = self.tblResult.horizontalHeaderItem(1)
        item.setText(_translate("InfoSearch", "XML Filename"))

import rsrc_rc
