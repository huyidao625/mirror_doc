#!/usr/bin/env python
#coding=utf-8
#python 2.7.5
'''
@since: 2018-07-25 13:48:58
@author: hufei
@version: 1.0
@note: project Module
'''
class project:
    def __init__(self):
        self.id = None     #int(11)  #工程编号
        self.name = None     #varchar(45)  #工程名称
        self.path = None     #varchar(200)  #工程路径
        self.desc = None     #varchar(300)  #工程描述
        self.isdelete = None     #int(11)  #是否删除工程
