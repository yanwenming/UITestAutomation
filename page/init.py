#!/usr/bin/env python
# -*-coding:utf-8-*-

#author:Yan Wenming
#create time:2019-07-08

import unittest
from selenium import webdriver
from utils.operationXml import *


class Init(unittest.TestCase,OperationXml):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')

    def tearDown(self):
        self.driver.quit()