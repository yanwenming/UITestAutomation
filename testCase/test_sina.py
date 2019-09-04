#!/usr/bin/env python
# -*-coding:utf-8-*-

#author:Yan Wenming
#create time:2019-07-08

import unittest
from page.sina import *
from page.init import *
import time as t


class SinaTest(Init,Sina):
    def test_sinaLogin_001( self,parent='divText',value='emailNull' ):
        '''登录页面：账号密码为空验证'''
        self.login('','')
        self.assertEqual(self.getLoginError,self.getXmlUser(parent,value))

    def test_sinaLogin_002( self,parent='divText',value='emailFormat' ):
        ''''''
        self.login('yanweming','123456')
        self.assertEqual(self.getLoginError,self.getXmlUser(parent,value))


if __name__ == '__main__':
    unittest.main(verbosity = 2)



