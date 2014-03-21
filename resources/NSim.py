__author__ = 'Abraham Aondowase Yusuf <yabraham@swglobal.com>'

import os
import sys
import zipfile
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Ui_Nsim import Ui_NSim
from datastructures import FEPRecord

class NSim(QtWidgets.QFrame, Ui_NSim):

    def __init__(self, parent=None):
        super(NSim, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)
        self.lblCurPos.setVisible(False)
        self.setMinimumSize(QtCore.QSize(1200, 500))

        self.foundItems = []
        self.currentPos = 0
        self.fepSearchPath = QtCore.QSettings().value('FEPSearchPath', None)
        if self.fepSearchPath:
            self.txtFEPFolder.setText(self.fepSearchPath)


    @QtCore.pyqtSlot()
    def on_btnFEPFolder_clicked(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.txtFEPFolder.setText(folder)

        self.fepSearchPath = folder
        QtCore.QSettings().setValue('FEPSearchPath', folder)

    @QtCore.pyqtSlot()
    def on_btnFind_clicked(self):
        if self.txtSearch.text().strip() == '':
            QtWidgets.QMessageBox.information(self, 'Info', 'You have not entered a file name.')
            return

        testString = self.txtSearch.text().strip()
        self.foundItems = []  # list of tuples in the form (zipfile, xmlfile)

        zfiles = [os.path.join(self.fepSearchPath, i) for i in os.listdir(self.fepSearchPath) if i.lower().endswith('.zip')]
        for zfile in zfiles:
            try:
                with zipfile.ZipFile(zfile) as z:
                    xmls = [i for i in z.namelist() if i.lower().endswith('.xml')]
            except Exception as e:
                sys.stderr.write(repr(e))
            self.foundItems.extend([(zfile, i) for i in xmls if testString in i])

        QtWidgets.QMessageBox.information(self, 'Search Completed', 'Found %s items.' % self._countFoundItems())
        self.currentPos = 0
        self._showItem()

    @QtCore.pyqtSlot()
    def on_btnFirst_clicked(self):
        self.currentPos = 0
        self._showItem()

    @QtCore.pyqtSlot()
    def on_btnLast_clicked(self):
        self.currentPos = len(self.foundItems) - 1
        self._showItem()

    @QtCore.pyqtSlot()
    def on_btnPrev_clicked(self):
        if self.currentPos == 0:
            return
        self.currentPos -= 1
        self._showItem()

    @QtCore.pyqtSlot()
    def on_btnNext_clicked(self):
        if self.currentPos == len(self.foundItems) - 1:
            return
        self.currentPos += 1
        self._showItem()

    def _countFoundItems(self):
        return len(self.foundItems)

    def _showItem(self):
        if not len(self.foundItems) or self.currentPos > len(self.foundItems) or self.currentPos < 0:
            self.currentPos = 0
            return

        zipf, xmlf = self.foundItems[self.currentPos]
        item = FEPRecord(zipf, xmlf)

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

        self.lblCurPos.setText('%s of %s' % (self.currentPos + 1, len(self.foundItems)))
        self.lblCurPos.setVisible(True)

        #leftThumb = QtGui.QPixmap()
        #leftThumb.loadFromData(item.LeftThumbPrint.FingerprintImage, 'WSQ')
        #self.lblLeftThumbPrint.setPixmap(leftThumb)