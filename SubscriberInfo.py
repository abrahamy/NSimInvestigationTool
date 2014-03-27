__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import os
import logging

from PyQt5 import QtCore, QtWidgets, QtPrintSupport

from datastructures import FEPRecord

from ui_SubscriberInfo import Ui_SubscriberInfo


class SubscriberInfo(QtWidgets.QDialog, Ui_SubscriberInfo):

    def __init__(self, subscriber_info, parent=None):
        super(SubscriberInfo, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)
        self.logger = logging.getLogger(__name__)

        self.search_path = os.path.join(os.path.dirname(__file__), 'resources')
        self.html_filename = 'subscriber-info.html'

        self.textBrowser.setSearchPaths([self.search_path])

        self.render_template(subscriber_info)

    @QtCore.pyqtSlot()
    def on_btnPrint_clicked(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)

        print_dialog = QtPrintSupport.QPrintDialog(printer, self)
        print_dialog.setWindowTitle('Print Subscriber Information')

        if print_dialog.exec() != QtWidgets.QDialog.Accepted:
            return

        printer.setFullPage(True)
        printer.setPageSize(QtPrintSupport.QPrinter.A4)

        self.textBrowser.document().print(printer)
        self.accept()

    def render_template(self, subscriber):
        if not isinstance(subscriber, FEPRecord):
            self.logger.error('TypeError: Subscriber must be an instance of FEPRecord')
            return

        template_name = os.path.join(os.path.dirname(__file__), 'resources', 'template.html')
        try:
            with open(template_name, 'r') as template:
                html = template.read().strip()

        except Exception as e:
            self.logger.error('Error: %s\tTemplate File: %s' % (repr(e), template_name))
            return

        html.replace('{{packet}}', subscriber.packet_name)
        html.replace('{{photo_uri}}', self.write_image_data(subscriber._PotraitImage))
        html.replace('{{xml_file}}', subscriber.xml_filename)
        html.replace('{{fep_code}}', subscriber.FEPCode)
        html.replace('{{fep_tracking_id}}', subscriber.FEPTrackingID)
        html.replace('{{registration_type}}', subscriber.RegistrationType)
        html.replace('{{folio_version}}', subscriber.FolioVersion)
        html.replace('{{subscriber_id}}', subscriber.SubscriberID)
        html.replace('{{registration_date}}', subscriber.RegistrationDate)
        html.replace('{{registration_time}}', subscriber.RegistrationTime)
        html.replace('{{registration_state}}', subscriber.RegistrationState)
        html.replace('{{registration_lga}}', subscriber.RegistrationLGA)
        html.replace('{{surname}}', subscriber.Surname)
        html.replace('{{first_name}}', subscriber.FirstName)
        html.replace('{{mothers_maiden_name}}', subscriber.MotherMaidenName)
        html.replace('{{gender}}', subscriber.Gender)
        html.replace('{{date_of_birth}}', subscriber.DateOfBirth)
        html.replace('{{residential_address}}', subscriber.ResidentialAddress)
        html.replace('{{residential_address_state}}', subscriber.ResidentialAddressState)
        html.replace('{{residential_address_lga}}', subscriber.ResidentialAddressLGA)
        html.replace('{{nationality}}', subscriber.Nationality)
        html.replace('{{state_of_origin}}', subscriber.StateofOrigin)
        html.replace('{{main_mobile_number}}', subscriber.MainMobileNumber)
        html.replace('{{other_mobile_numbers}}', subscriber.OtherMobileNumbers)

        try:
            with open(os.path.join(self.search_path, self.html_filename), 'w') as outfile:
                outfile.write(html)

            self.textBrowser.setSource(QtCore.QUrl(self.html_filename))

        except Exception as e:
            self.logger.error(repr(e))

    def write_image_data(self, image_data):
        filename = os.path.join(os.path.dirname(__file__), 'resources', 'passport.jpg')
        try:
            with open(filename, 'wb') as image_file:
                image_file.write(image_data)

            return filename

        except Exception as e:
            self.logger.error(repr(e))
            return ''