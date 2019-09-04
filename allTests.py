#!/usr/bin/env python
# -*-coding:utf-8-*-

#author:Yan Wenming
#create time:2019-07-08


import unittest
import os
import HTMLTestRunner
import time


def allTests():
    '''获取所有需要执行的测试用例'''
    suite = unittest.defaultTestLoader.discover(
        start_dir = os.path.join(os.path.dirname(__file__),'testCase'),
        pattern = 'test_*.py',
        top_level_dir = None
    )
    return suite


def getNowTime():
    '''获取当前时间'''
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))


def run():
    filename = os.path.join(os.path.dirname(__file__),'report',getNowTime()+'sinaReport.html')
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = 'UI自动化测试报告',
        description = 'UI自动化测试报告详细信息'
    )
    runner.run(allTests())


if __name__ == '__main__':
    run()