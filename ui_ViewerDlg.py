# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewerDlg.ui'
#
# Created: Mon Mar 17 16:12:57 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewerDlg(object):
    def setupUi(self, ViewerDlg):
        ViewerDlg.setObjectName("ViewerDlg")
        ViewerDlg.resize(1011, 404)
        ViewerDlg.setMaximumSize(QtCore.QSize(1011, 404))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(ViewerDlg)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(ViewerDlg)
        self.groupBox.setMinimumSize(QtCore.QSize(991, 351))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txtStateOfOrigin = QtWidgets.QLineEdit(self.groupBox)
        self.txtStateOfOrigin.setMinimumSize(QtCore.QSize(138, 0))
        self.txtStateOfOrigin.setReadOnly(True)
        self.txtStateOfOrigin.setObjectName("txtStateOfOrigin")
        self.gridLayout_2.addWidget(self.txtStateOfOrigin, 8, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 8, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 10, 0, 1, 1)
        self.txtFirstName = QtWidgets.QLineEdit(self.groupBox)
        self.txtFirstName.setMinimumSize(QtCore.QSize(277, 0))
        self.txtFirstName.setReadOnly(True)
        self.txtFirstName.setObjectName("txtFirstName")
        self.gridLayout_2.addWidget(self.txtFirstName, 1, 3, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.lblPortraitData = QtWidgets.QLabel(self.groupBox)
        self.lblPortraitData.setMinimumSize(QtCore.QSize(140, 120))
        self.lblPortraitData.setMaximumSize(QtCore.QSize(140, 120))
        self.lblPortraitData.setText("")
        self.lblPortraitData.setPixmap(QtGui.QPixmap(":/images/person.png"))
        self.lblPortraitData.setScaledContents(True)
        self.lblPortraitData.setObjectName("lblPortraitData")
        self.gridLayout_2.addWidget(self.lblPortraitData, 0, 5, 5, 1)
        self.txtResidentialAddress = QtWidgets.QLineEdit(self.groupBox)
        self.txtResidentialAddress.setMinimumSize(QtCore.QSize(277, 0))
        self.txtResidentialAddress.setReadOnly(True)
        self.txtResidentialAddress.setObjectName("txtResidentialAddress")
        self.gridLayout_2.addWidget(self.txtResidentialAddress, 5, 3, 1, 2)
        self.txtFolioVersion = QtWidgets.QLineEdit(self.groupBox)
        self.txtFolioVersion.setMinimumSize(QtCore.QSize(277, 0))
        self.txtFolioVersion.setReadOnly(True)
        self.txtFolioVersion.setObjectName("txtFolioVersion")
        self.gridLayout_2.addWidget(self.txtFolioVersion, 3, 1, 1, 1)
        self.txtNationality = QtWidgets.QLineEdit(self.groupBox)
        self.txtNationality.setMinimumSize(QtCore.QSize(138, 0))
        self.txtNationality.setReadOnly(True)
        self.txtNationality.setObjectName("txtNationality")
        self.gridLayout_2.addWidget(self.txtNationality, 9, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.txtRegistrationType = QtWidgets.QLineEdit(self.groupBox)
        self.txtRegistrationType.setMinimumSize(QtCore.QSize(277, 0))
        self.txtRegistrationType.setReadOnly(True)
        self.txtRegistrationType.setObjectName("txtRegistrationType")
        self.gridLayout_2.addWidget(self.txtRegistrationType, 2, 1, 1, 1)
        self.txtMotherMaidenName = QtWidgets.QLineEdit(self.groupBox)
        self.txtMotherMaidenName.setMinimumSize(QtCore.QSize(277, 0))
        self.txtMotherMaidenName.setReadOnly(True)
        self.txtMotherMaidenName.setObjectName("txtMotherMaidenName")
        self.gridLayout_2.addWidget(self.txtMotherMaidenName, 2, 3, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 3, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 7, 2, 1, 1)
        self.txtRegistrationState = QtWidgets.QLineEdit(self.groupBox)
        self.txtRegistrationState.setMinimumSize(QtCore.QSize(277, 0))
        self.txtRegistrationState.setReadOnly(True)
        self.txtRegistrationState.setObjectName("txtRegistrationState")
        self.gridLayout_2.addWidget(self.txtRegistrationState, 7, 1, 1, 1)
        self.txtFEPTrackingID = QtWidgets.QLineEdit(self.groupBox)
        self.txtFEPTrackingID.setMinimumSize(QtCore.QSize(277, 0))
        self.txtFEPTrackingID.setReadOnly(True)
        self.txtFEPTrackingID.setObjectName("txtFEPTrackingID")
        self.gridLayout_2.addWidget(self.txtFEPTrackingID, 1, 1, 1, 1)
        self.txtSurname = QtWidgets.QLineEdit(self.groupBox)
        self.txtSurname.setMinimumSize(QtCore.QSize(277, 0))
        self.txtSurname.setReadOnly(True)
        self.txtSurname.setObjectName("txtSurname")
        self.gridLayout_2.addWidget(self.txtSurname, 0, 3, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 2, 1, 1)
        self.txtRegistrationLGA = QtWidgets.QLineEdit(self.groupBox)
        self.txtRegistrationLGA.setMinimumSize(QtCore.QSize(277, 0))
        self.txtRegistrationLGA.setReadOnly(True)
        self.txtRegistrationLGA.setObjectName("txtRegistrationLGA")
        self.gridLayout_2.addWidget(self.txtRegistrationLGA, 8, 1, 1, 1)
        self.txtMainMobileNumber = QtWidgets.QLineEdit(self.groupBox)
        self.txtMainMobileNumber.setMinimumSize(QtCore.QSize(138, 0))
        self.txtMainMobileNumber.setReadOnly(True)
        self.txtMainMobileNumber.setObjectName("txtMainMobileNumber")
        self.gridLayout_2.addWidget(self.txtMainMobileNumber, 10, 1, 1, 1)
        self.txtResidentialAddressLGA = QtWidgets.QLineEdit(self.groupBox)
        self.txtResidentialAddressLGA.setMinimumSize(QtCore.QSize(138, 0))
        self.txtResidentialAddressLGA.setReadOnly(True)
        self.txtResidentialAddressLGA.setObjectName("txtResidentialAddressLGA")
        self.gridLayout_2.addWidget(self.txtResidentialAddressLGA, 6, 3, 1, 2)
        self.txtResidentialAddressState = QtWidgets.QLineEdit(self.groupBox)
        self.txtResidentialAddressState.setMinimumSize(QtCore.QSize(138, 0))
        self.txtResidentialAddressState.setReadOnly(True)
        self.txtResidentialAddressState.setObjectName("txtResidentialAddressState")
        self.gridLayout_2.addWidget(self.txtResidentialAddressState, 7, 3, 1, 2)
        self.txtRegistrationDate = QtWidgets.QLineEdit(self.groupBox)
        self.txtRegistrationDate.setMinimumSize(QtCore.QSize(277, 0))
        self.txtRegistrationDate.setReadOnly(True)
        self.txtRegistrationDate.setObjectName("txtRegistrationDate")
        self.gridLayout_2.addWidget(self.txtRegistrationDate, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.txtSubscriberID = QtWidgets.QLineEdit(self.groupBox)
        self.txtSubscriberID.setMinimumSize(QtCore.QSize(277, 0))
        self.txtSubscriberID.setReadOnly(True)
        self.txtSubscriberID.setObjectName("txtSubscriberID")
        self.gridLayout_2.addWidget(self.txtSubscriberID, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 4, 2, 1, 1)
        self.txtGender = QtWidgets.QLineEdit(self.groupBox)
        self.txtGender.setMinimumSize(QtCore.QSize(277, 0))
        self.txtGender.setReadOnly(True)
        self.txtGender.setObjectName("txtGender")
        self.gridLayout_2.addWidget(self.txtGender, 3, 3, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 6, 2, 1, 1)
        self.txtRegistrationTime = QtWidgets.QLineEdit(self.groupBox)
        self.txtRegistrationTime.setMinimumSize(QtCore.QSize(277, 0))
        self.txtRegistrationTime.setReadOnly(True)
        self.txtRegistrationTime.setObjectName("txtRegistrationTime")
        self.gridLayout_2.addWidget(self.txtRegistrationTime, 6, 1, 1, 1)
        self.txtDateOfBirth = QtWidgets.QLineEdit(self.groupBox)
        self.txtDateOfBirth.setMinimumSize(QtCore.QSize(277, 0))
        self.txtDateOfBirth.setReadOnly(True)
        self.txtDateOfBirth.setObjectName("txtDateOfBirth")
        self.gridLayout_2.addWidget(self.txtDateOfBirth, 4, 3, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 5, 2, 1, 1)
        self.txtFepCode = QtWidgets.QLineEdit(self.groupBox)
        self.txtFepCode.setMinimumSize(QtCore.QSize(277, 0))
        self.txtFepCode.setReadOnly(True)
        self.txtFepCode.setObjectName("txtFepCode")
        self.gridLayout_2.addWidget(self.txtFepCode, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 9, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 8, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(718, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnPrint = QtWidgets.QPushButton(ViewerDlg)
        self.btnPrint.setObjectName("btnPrint")
        self.horizontalLayout.addWidget(self.btnPrint)
        self.btnClose = QtWidgets.QPushButton(ViewerDlg)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.label_3.setBuddy(self.txtFEPTrackingID)
        self.label_20.setBuddy(self.txtStateOfOrigin)
        self.label_21.setBuddy(self.txtMainMobileNumber)
        self.label_7.setBuddy(self.txtRegistrationDate)
        self.label_4.setBuddy(self.txtRegistrationType)
        self.label_13.setBuddy(self.txtMotherMaidenName)
        self.label_5.setBuddy(self.txtFolioVersion)
        self.label_14.setBuddy(self.txtGender)
        self.label_18.setBuddy(self.txtResidentialAddressState)
        self.label_11.setBuddy(self.txtSurname)
        self.label_12.setBuddy(self.txtFirstName)
        self.label_6.setBuddy(self.txtSubscriberID)
        self.label_15.setBuddy(self.txtDateOfBirth)
        self.label_17.setBuddy(self.txtResidentialAddressLGA)
        self.label_8.setBuddy(self.txtRegistrationTime)
        self.label_16.setBuddy(self.txtResidentialAddress)
        self.label_2.setBuddy(self.txtFepCode)
        self.label_19.setBuddy(self.txtNationality)
        self.label_9.setBuddy(self.txtRegistrationState)
        self.label_10.setBuddy(self.txtRegistrationLGA)

        self.retranslateUi(ViewerDlg)
        self.btnClose.clicked.connect(ViewerDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ViewerDlg)

    def retranslateUi(self, ViewerDlg):
        _translate = QtCore.QCoreApplication.translate
        ViewerDlg.setWindowTitle(_translate("ViewerDlg", "NSIM Demographics Viewer :: Details"))
        self.groupBox.setTitle(_translate("ViewerDlg", "Registration Details"))
        self.label_3.setText(_translate("ViewerDlg", "FEP Tracking ID:"))
        self.label_20.setText(_translate("ViewerDlg", "State of Origin:"))
        self.label_21.setText(_translate("ViewerDlg", "Main Mobile Number:"))
        self.label_7.setText(_translate("ViewerDlg", "Registration Date:"))
        self.label_4.setText(_translate("ViewerDlg", "Registration Type:"))
        self.label_13.setText(_translate("ViewerDlg", "Mother\'s Maiden Name:"))
        self.label_5.setText(_translate("ViewerDlg", "Folio Version:"))
        self.label_14.setText(_translate("ViewerDlg", "Gender:"))
        self.label_18.setText(_translate("ViewerDlg", "Residential Address State:"))
        self.label_11.setText(_translate("ViewerDlg", "Surname:"))
        self.label_12.setText(_translate("ViewerDlg", "First Name:"))
        self.label_6.setText(_translate("ViewerDlg", "Subscriber ID:"))
        self.label_15.setText(_translate("ViewerDlg", "Date of Birth:"))
        self.label_17.setText(_translate("ViewerDlg", "Residential Address LGA:"))
        self.label_8.setText(_translate("ViewerDlg", "Registration Time:"))
        self.label_16.setText(_translate("ViewerDlg", "Residential Address:"))
        self.label_2.setText(_translate("ViewerDlg", "FEP Code:"))
        self.label_19.setText(_translate("ViewerDlg", "Nationality:"))
        self.label_9.setText(_translate("ViewerDlg", "Registration State:"))
        self.label_10.setText(_translate("ViewerDlg", "Registration LGA:"))
        self.btnPrint.setText(_translate("ViewerDlg", "&Print"))
        self.btnClose.setText(_translate("ViewerDlg", "&Close"))

import resources_rc
