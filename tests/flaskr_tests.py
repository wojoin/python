# -*- coding: utf-8 -*-
# Project Name  : Python 
# File Name     : flaskr_tests.py
# Author        : 细嗅蔷薇
# Date Time     : 2016/9/27 22:04
# Description   :flaskr的单元测试
# Version       : 1.0.1


import os
import flaskr
import unittest
import tempfile


from sys import path
for fp in path:
    print(fp)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()


