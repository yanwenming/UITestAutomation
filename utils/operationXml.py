#!/usr/bin/env python
# -*-coding:utf-8-*-

#author:Yan Wenming
#create time:2019-07-08

import os
import xml.dom.minidom


class OperationXml(object):
    def dir_base(self,filename,filePath = 'data'):
        '''
        获取data 文件夹下的文件
        :param filename:要读的文件名
        :param filePath:要读的文件对应的文件夹
        :return:
        '''
        return os.path.join(os.path.dirname(
            os.path.dirname(__file__)),filePath,filename)

    def getXmlData(self,value):
        '''
        获取xml单个节点的数据
        :param value:xml文件中单个节点的名称
        :return:
        '''
        dom = xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        namevalue =name[0]
        print('namevalue的内容为{0}'.format(namevalue))
        return namevalue.firstChild.data

    def getXmlUser(self,parent,child):
        '''
        获取xml子节点的数据
        :param parent:xml文件中父节点的名称
        :param child:xml文件中子节点的名称
        :return:
        '''
        dom = xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db = dom.documentElement
        itemlist = db.getElementsByTagName(parent)
        item = itemlist[0]
        return item.getAttribute(child)

