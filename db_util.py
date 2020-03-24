# -*- coding: utf-8 -*-
# module db_util
# Created on 2020/3/24 10:36

import MySQLdb


class DBUtil:
    def __init__(self, db):
        self.db = MySQLdb.connect(host=db['HOST'], user=db['USER'], passwd=db['PASSWD'], db=db['DB'],
                                  charset=db['CHARSET'], port=db['PORT'])

    def execute(self, sql):
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)
        self.db.commit()
