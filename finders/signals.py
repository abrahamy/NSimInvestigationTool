__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

from PyQt5 import QtCore


class SignalFactory(QtCore.QObject):
    statusChanged = QtCore.pyqtSignal(int, int)
    completed = QtCore.pyqtSignal()
    completedWithResult = QtCore.pyqtSignal(tuple)
    itemFound = QtCore.pyqtSignal(str, str, name='itemFound')  # arg1: packetName, arg2: xmlFileName
    info = QtCore.pyqtSignal(str)
