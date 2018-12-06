#!/usr/bin/env python
#coding=utf-8
#python 2.7.5
'''
@since: 2018-07-25 08:37:57
@author: hufei
@copyright: The content of this file is subject to the Romtek  Innovation Company.
@contact: The Initial Developer of the Original Code is department of CFD ,Romtek  Innovation Company,having its main offices at:  Room 907,Building No.1,Boya International Center,Wangjing,Chaoyang District,Beijing,China.(100102).
          Tel:+(86)10-84782838/84782018
          mail:info@romtek.cn
@version: 1.0
@note: resourcemachine Module
'''
class resourcemachine:
    def __init__(self):
        self.id = None     #int(11)  #b''
        self.name = None     #varchar(45)  #b''
        self.ip = None     #varchar(45)  #b''
        self.avaiable_core = None     #int(11)  #b''
        self.used_core = None     #int(11)  #b''
        self.type = None     #varchar(45)  #b''
        self.hardware_info = None     #varchar(1000)  #b''
        self.status = None     #varchar(45)  #b''
        self.isdelete = None     #int(11)  #b''
