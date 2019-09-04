#!/usr/bin/env python
# -*-coding:utf-8-*-

#author:Yan Wenming
#create time:2019-07-08

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import \
    NoSuchElementException
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class Factory(object):
    def __init__(self,driver):
        self.driver = driver
    #工厂方法

    def createDriver( self,driver ):
        if driver == 'web':
            return WebUI(self.driver)
        if driver == 'App':
            return AppUI(self.driver)

class WebDriver(object):
    '''单个定位元素的方法'''
    def __init__(self,driver):
        self.driver = driver

    def findElement( self,*loc ):
        try:
            # return self.driver.find_element(*loc)
            return WebDriverWait(self.driver,20).until(lambda x: x.find_element(*loc))

        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def findElements( self,*loc ):
        '''多个定位元素的方法'''
        try:
            return WebDriverWait(self.driver , 20).until(lambda x: x.find_elements(*loc))
            # return self.driver.find_elements(*loc)
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))


class WebUI(WebDriver):
    def __str__(self):
        return 'WebUI'


class AppUI(WebDriver):
    def __str__(self):
        return 'AppUI'