# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchForm.ui'
#
# Created: Wed Mar 26 11:21:39 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        SearchForm.setObjectName("SearchForm")
        SearchForm.resize(640, 480)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SearchForm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblMessage = QtWidgets.QLabel(SearchForm)
        self.lblMessage.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: italic 10pt \"Segoe UI\";")
        self.lblMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout_3.addWidget(self.lblMessage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblMobileNos = QtWidgets.QLabel(SearchForm)
        self.lblMobileNos.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        self.lblMobileNos.setObjectName("lblMobileNos")
        self.verticalLayout.addWidget(self.lblMobileNos)
        self.txtMobileNos = QtWidgets.QTextEdit(SearchForm)
        self.txtMobileNos.setObjectName("txtMobileNos")
        self.verticalLayout.addWidget(self.txtMobileNos)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGetFile = QtWidgets.QPushButton(SearchForm)
        self.btnGetFile.setStyleSheet("color: rgb(5, 17, 127);\n"
"text-decoration: underline;\n"
"font: 10pt \"Segoe UI\";")
        self.btnGetFile.setFlat(True)
        self.btnGetFile.setObjectName("btnGetFile")
        self.horizontalLayout.addWidget(self.btnGetFile)
        self.btnSearch = QtWidgets.QPushButton(SearchForm)
        self.btnSearch.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.lblStatus = QtWidgets.QLabel(SearchForm)
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
        self.lblResult = QtWidgets.QLabel(SearchForm)
        self.lblResult.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 10pt \"Segoe UI\";")
        self.lblResult.setObjectName("lblResult")
        self.verticalLayout_2.addWidget(self.lblResult)
        self.tblResult = QtWidgets.QTableView(SearchForm)
        self.tblResult.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblResult.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblResult.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblResult.setObjectName("tblResult")
        self.verticalLayout_2.addWidget(self.tblResult)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(SearchForm)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)
        SearchForm.setTabOrder(self.txtMobileNos, self.btnGetFile)
        SearchForm.setTabOrder(self.btnGetFile, self.btnSearch)
        SearchForm.setTabOrder(self.btnSearch, self.tblResult)

    def retranslateUi(self, SearchForm):
        _translate = QtCore.QCoreApplication.translate
        SearchForm.setWindowTitle(_translate("SearchForm", "Find Packet Names"))
        self.lblMessage.setText(_translate("SearchForm", "Enter a comma separated list of mobile numbers in the textbox below or click on \"Import From File\" to import from a text file."))
        self.lblMobileNos.setText(_translate("SearchForm", "Mobile Numbers:"))
        self.btnGetFile.setText(_translate("SearchForm", "Import From File"))
        self.btnSearch.setText(_translate("SearchForm", "Search"))
        self.lblStatus.setText(_translate("SearchForm", "Loading"))
        self.lblResult.setText(_translate("SearchForm", "List of Items Found:"))

import rsrc_rc
