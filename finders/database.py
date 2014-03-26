__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import os

import pymssql
from PyQt5 import QtCore

from .signals import SignalFactory


query = ("SELECT\n"
         "\tT3.[mobileNumber], T2.[packetName], T1.[fileName]\n"
         "FROM\n\tR_Registration AS T1\n"
         "LEFT JOIN\n\t(R_Packet AS T2 CROSS JOIN R_MobileNumber AS T3)\n"
         "ON\n\t(T1.[packet_id] = T2.[id] AND T1.[id] = T3.[registration_id])\n"
         "WHERE\n\tT1.[id] IN (\n"
         "\t\tSELECT R_MobileNumber.[registration_id] FROM R_MobileNumber WHERE R_MobileNumber.[mobileNumber] IN (%s)"
         "\n\t)").join('')

connection_str = os.environ.get('MSSQL_CONN', 'localhost;user;password;testdb')


class DatabaseFinder(QtCore.QRunnable):

    def __init__(self, task):
        super(DatabaseFinder, self).__init__()

        self.mobile_numbers = task.mobile_numbers
        self.signals = SignalFactory()

    def run(self):
        self.signals.info.emit('Database search started')
        try:
            server, user, password, db = connection_str.split(';')
            with pymssql.connect(server, user, password, db) as conn:
                with conn.cursor as cursor:
                    cursor.execute(query % ["'%s'" % i for i in self.mobile_numbers].join(','))

                    result = []
                    for row in cursor.fetchall():
                        result.append(row)

                    self.signals.completedWithResult.emit(tuple(result))

        except Exception as e:
            self.signals.info.emit('Encountered and error in database search. Error Message: [%s]' % repr(e))
