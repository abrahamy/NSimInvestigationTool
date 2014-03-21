__author__ = 'Administrator'

from PyQt5 import QtWidgets, QtGui

from ui_ViewerDlg import Ui_ViewerDlg

class ViewerDlg(QtWidgets.QDialog, Ui_ViewerDlg):

    def __init__(self, parent=None, item=None):
        super(ViewerDlg, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)
        self.btnPrint.setVisible(False)

        if item:
            self.populateData(item)

    def populateData(self, item):
        self.txtFepCode.setText(item.FEPCode)
        self.txtFEPTrackingID.setText(item.FEPTrackingID)
        self.txtRegistrationType.setText(item.RegistrationType)
        self.txtFolioVersion.setText(item.FolioVersion)
        self.txtSubscriberID.setText(item.SubscriberID)
        self.txtRegistrationDate.setText(item.RegistrationDate)
        self.txtRegistrationTime.setText(item.RegistrationTime)
        self.txtRegistrationState.setText(item.RegistrationState)
        self.txtRegistrationLGA.setText(item.RegistrationLGA)
        self.txtSurname.setText(item.Surname)
        self.txtFirstName.setText(item.FirstName)
        self.txtMotherMaidenName.setText(item.MotherMaidenName)
        self.txtGender.setText(item.Gender)
        self.txtDateOfBirth.setText(item.DateOfBirth)
        self.txtResidentialAddress.setText(item.ResidentialAddress)
        self.txtResidentialAddressLGA.setText(item.ResidentialAddressLGA)
        self.txtResidentialAddressState.setText(item.ResidentialAddressState)
        self.txtNationality.setText(item.Nationality)
        self.txtStateOfOrigin.setText(item.StateofOrigin)
        self.txtMainMobileNumber.setText(item.MainMobileNumber)

        portrait = QtGui.QPixmap()
        portrait.loadFromData(item.PortraitData.PortraitImage, item.PortraitData.ImageType)
        self.lblPortraitData.setPixmap(portrait)