# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBSearch.ui'
#
# Created: Wed Mar 26 14:39:52 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DBSearch(object):
    def setupUi(self, DBSearch):
        DBSearch.setObjectName("DBSearch")
        DBSearch.resize(640, 480)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DBSearch)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblMessage = QtWidgets.QLabel(DBSearch)
        self.lblMessage.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: italic 10pt \"Segoe UI\";")
        self.lblMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout_3.addWidget(self.lblMessage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblMobileNos = QtWidgets.QLabel(DBSearch)
        self.lblMobileNos.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        self.lblMobileNos.setObjectName("lblMobileNos")
        self.verticalLayout.addWidget(self.lblMobileNos)
        self.txtMobileNos = QtWidgets.QTextEdit(DBSearch)
        self.txtMobileNos.setObjectName("txtMobileNos")
        self.verticalLayout.addWidget(self.txtMobileNos)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGetFile = QtWidgets.QPushButton(DBSearch)
        self.btnGetFile.setStyleSheet("color: rgb(5, 17, 127);\n"
"text-decoration: underline;\n"
"font: 10pt \"Segoe UI\";")
        self.btnGetFile.setFlat(True)
        self.btnGetFile.setObjectName("btnGetFile")
        self.horizontalLayout.addWidget(self.btnGetFile)
        self.btnSearch = QtWidgets.QPushButton(DBSearch)
        self.btnSearch.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.lblStatus = QtWidgets.QLabel(DBSearch)
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
        self.lblResult = QtWidgets.QLabel(DBSearch)
        self.lblResult.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        self.lblResult.setObjectName("lblResult")
        self.verticalLayout_2.addWidget(self.lblResult)
        self.txtResult = QtWidgets.QTextEdit(DBSearch)
        self.txtResult.setReadOnly(True)
        self.txtResult.setObjectName("txtResult")
        self.verticalLayout_2.addWidget(self.txtResult)
        self.btnSaveAs = QtWidgets.QPushButton(DBSearch)
        self.btnSaveAs.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        self.btnSaveAs.setObjectName("btnSaveAs")
        self.verticalLayout_2.addWidget(self.btnSaveAs)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(DBSearch)
        QtCore.QMetaObject.connectSlotsByName(DBSearch)
        DBSearch.setTabOrder(self.txtMobileNos, self.btnGetFile)
        DBSearch.setTabOrder(self.btnGetFile, self.btnSearch)

    def retranslateUi(self, DBSearch):
        _translate = QtCore.QCoreApplication.translate
        DBSearch.setWindowTitle(_translate("DBSearch", "Find Packet Names"))
        self.lblMessage.setText(_translate("DBSearch", "Enter a comma separated list of mobile numbers in the textbox below or click on \"Import From File\" to import from a text file."))
        self.lblMobileNos.setText(_translate("DBSearch", "Mobile Numbers:"))
        self.btnGetFile.setText(_translate("DBSearch", "Import From File"))
        self.btnSearch.setText(_translate("DBSearch", "Search"))
        self.lblStatus.setText(_translate("DBSearch", "Loading"))
        self.lblResult.setText(_translate("DBSearch", "List of Items Found:"))
        self.btnSaveAs.setText(_translate("DBSearch", "Save Result As.."))

import rsrc_rc
