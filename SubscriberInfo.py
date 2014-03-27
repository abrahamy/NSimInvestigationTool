__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import os
import logging

from jinja2 import Template
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

        template = Template(html)
        data = dict(
            packet=subscriber.packet_name, photo_uri=self.write_image_data(subscriber._PotraitImage),
            xml_file=subscriber.xml_filename, fep_code=subscriber.FEPCode, fep_tracking_id=subscriber.FEPTrackingID,
            registration_type=subscriber.RegistrationType, folio_version=subscriber.FolioVersion,
            subscriber_id=subscriber.SubscriberID, registration_date=subscriber.RegistrationDate,
            registration_time=subscriber.RegistrationTime, registration_state=subscriber.RegistrationState,
            registration_lga=subscriber.RegistrationLGA, surname=subscriber.Surname, first_name=subscriber.FirstName,
            mothers_maiden_name=subscriber.MotherMaidenName, gender=subscriber.Gender,
            date_of_birth=subscriber.DateOfBirth, residential_address=subscriber.ResidentialAddress,
            residential_address_state=subscriber.ResidentialAddressState,
            residential_address_lga=subscriber.ResidentialAddressLGA, nationality=subscriber.Nationality,
            state_of_origin=subscriber.StateofOrigin, main_mobile_number=subscriber.MainMobileNumber,
            other_mobile_numbers=subscriber.OtherMobileNumbers
        )

        try:
            with open(os.path.join(self.search_path, self.html_filename), 'w') as outfile:
                outfile.write(template.render(data))

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