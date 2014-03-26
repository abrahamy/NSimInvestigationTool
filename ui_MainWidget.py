# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\MainWidget.ui'
#
# Created: Wed Mar 26 13:15:00 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(640, 480)
        self.tabWelcome = QtWidgets.QWidget()
        self.tabWelcome.setObjectName("tabWelcome")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabWelcome)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.tabWelcome)
        self.label.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 75 14pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btnDbSearch = QtWidgets.QPushButton(self.tabWelcome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDbSearch.sizePolicy().hasHeightForWidth())
        self.btnDbSearch.setSizePolicy(sizePolicy)
        self.btnDbSearch.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 75 10pt \"Segoe UI\";")
        self.btnDbSearch.setObjectName("btnDbSearch")
        self.horizontalLayout.addWidget(self.btnDbSearch)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.btnFileSystemSearch = QtWidgets.QPushButton(self.tabWelcome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFileSystemSearch.sizePolicy().hasHeightForWidth())
        self.btnFileSystemSearch.setSizePolicy(sizePolicy)
        self.btnFileSystemSearch.setStyleSheet("color: rgb(5, 17, 127);\n"
"font: 75 10pt \"Segoe UI\";")
        self.btnFileSystemSearch.setObjectName("btnFileSystemSearch")
        self.horizontalLayout_2.addWidget(self.btnFileSystemSearch)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 138, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWidget.addTab(self.tabWelcome, "")

        self.retranslateUi(MainWidget)
        MainWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "NSIM Investigation Tool"))
        self.label.setText(_translate("MainWidget", "NSIM Investigation Tool"))
        self.btnDbSearch.setText(_translate("MainWidget", "Search For Packet Names"))
        self.btnFileSystemSearch.setText(_translate("MainWidget", "Search For Subscriber Information"))
        MainWidget.setTabText(MainWidget.indexOf(self.tabWelcome), _translate("MainWidget", "Welcome"))

