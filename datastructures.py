__author__ = 'Abraham Aondowase Yusuf <yabraham@swglobal.com>'

import zipfile
from base64 import b64decode
from xml.etree import cElementTree as ET

class OperationError(Exception):
    pass

class PortraitData(object):

    def __init__(self, portraitImage, imageType, imageCompression, compressionRatio):
        self.PortraitImage = portraitImage
        self.ImageType = imageType
        self.ImageCompression = imageCompression
        self.CompressionRatio = compressionRatio


class FingerData(object):

    def __init__(self, fingerInfo, fingerReason, supervisorName, nfiq, wsqImageCompressionRatio, fingerprintImage):
        self.FingerInfo = fingerInfo
        self.FingerReason = fingerReason
        self.SupervisorName = supervisorName
        self.NFIQ = nfiq
        self.WSQImageCompressionRatio = wsqImageCompressionRatio
        self.FingerprintImage = fingerprintImage


class FEPRecord(object):

    def __getattr__(self, item):
        if hasattr(self, item):
            return getattr(self, item)

        if item in ['LeftThumbPrint', 'RightThumbPrint', 'LeftIndexFingerPrint', 'RightIndexFingerPrint']:
            for finger in self._fingers:
                if finger.FingerInfo == item:
                    return item
        raise AttributeError

    def __init__(self, zipf, xmlf):
        self.packet_name, self.xml_filename = zipf, xmlf
        try:
            with zipfile.ZipFile(zipf) as input:
                tree = ET.fromstring(input.open(xmlf).read())
        except ET.ParseError as e:
            raise OperationError('Invalid XML File')

        attrs = [
            ('FEPCode','.//NigeriaSIMDemographics/FEPCode', None),
            ('FEPTrackingID','.//NigeriaSIMDemographics/FEPTrackingID', None),
            ('RegistrationType', './/NigeriaSIMDemographics/RegistrationType', None),
            ('FolioVersion', './/NigeriaSIMDemographics/FolioVersion', None),
            ('SubscriberID', './/NigeriaSIMDemographics/SubscriberID', None),
            ('RegistrationDate', './/NigeriaSIMDemographics/RegistrationDate', None),
            ('RegistrationTime','.//NigeriaSIMDemographics/RegistrationTime', None),
            ('RegistrationState', './/NigeriaSIMDemographics/RegistrationState', None),
            ('RegistrationLGA', './/NigeriaSIMDemographics/RegistrationLGA', None),
            ('Surname', './/NigeriaSIMDemographics/Surname', None),
            ('FirstName', './/NigeriaSIMDemographics/FirstName', None),
            ('MotherMaidenName', './/NigeriaSIMDemographics/MotherMaidenName', None),
            ('Gender', './/NigeriaSIMDemographics/Gender', None),
            ('DateOfBirth', './/NigeriaSIMDemographics/DateOfBirth', None),
            ('ResidentialAddress', './/NigeriaSIMDemographics/ResidentialAddress', None),
            ('ResidentialAddressLGA', './/NigeriaSIMDemographics/ResidentialAddressLGA', None),
            ('ResidentialAddressState', './/NigeriaSIMDemographics/ResidentialAddressState', None),
            ('Nationality', './/NigeriaSIMDemographics/Nationality', None),
            ('StateofOrigin', './/NigeriaSIMDemographics/StateofOrigin', None),
            ('MainMobileNumber', './/NigeriaSIMDemographics/MainMobileNumber', None),
            ('OtherMobileNumbers', './/NigeriaSIMDemographics/OtherMobileNumbers', ''),
            ('_PotraitImage', './/NigeriaSIMDemographics/PortraitData/PotraitImage', None),
            ('_ImageType', './/NigeriaSIMDemographics/PortraitData/ImageType', None),
            ('_ImageCompression', './/NigeriaSIMDemographics/PortraitData/ImageCompression', None),
            ('_CompressionRatio', './/NigeriaSIMDemographics/PortraitData/CompressionRatio', None)
        ]

        for item in attrs:
            attr, path, default_value = item
            try:
                value = b64decode(tree.findall(path)[0].text) if attr in ['_PotraitImage'] else tree.findall(path)[0].text
                setattr(self, attr, value)
            except:
                setattr(self, attr, default_value or '')


        self.PortraitData = PortraitData(self._PotraitImage, self._ImageType, self._ImageCompression, self._CompressionRatio)

        self._fingers = []

        finger_attrs = [
            'FingerInfo', 'FingerReason', 'SupervisorName', 'NFIQ', 'WSQImageCompressionRatio', 'FingerprintImage'
        ]

        for f in tree.findall('.//NigeriaSIMDemographics/FingerData'):
            finger_args = []
            for attr in finger_attrs:
                try:
                    value = b64decode(f.findall(attr)[0].text) if attr in ['FingerprintImage'] else f.findall(attr)[0].text
                except:
                    value = ''

                finger_args.append(value)

            self._fingers.append(
                FingerData(*finger_args)
            )