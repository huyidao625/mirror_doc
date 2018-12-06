#!/usr/bin/env python
#coding=utf-8
#python 2.7.5
'''
@since: 2018-07-25 13:48:58
@author: hufei
@version: 1.0
@note: job Module
'''
class job:
    def __init__(self):
        self.id = None     #int(11)  #作业id,自增长
        self.name = None     #varchar(45)  #作业名称,根据多状态参数构建而成
        self.para = None     #text  #计算参数
        self.resourcemachine_id = None     #int(11)  #资源机id
        self.path = None     #varchar(200)  #作业运行路径,为资源机工作路径下的相对路径
        self.calcpackage_id = None     #int(11)  #计算包id
        self.pid = None     #varchar(45)  #
        self.attr = None     #varchar(200)  #
        self.project_id = None     #int(11)  #工程id
        self.process_info = None     #text  #过程信息
        self.result_info = None     #text  #结果信息
        self.type = None     #varchar(45)  #作业类型
        self.status = None     #varchar(45)  #作业状态
        self.isdelete = None     #int(11)  #是否删除
