Release Notes
=============

本文件版本发布日志, 记录每一个版本的更改情况.

Version 1.6.7a7
-------------------

Released: 2018-10-31

	
更新内容:
    
    * 新增消息的监控及返回值的监控 ,`配置文件说明 <http://192.168.2.100/mirrorgroup/mirror/wikis/%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E8%AF%B4%E6%98%8E>`_
    * 修复了杀作业与恢复作业的功能

.. warning::

    此版本新增了配置文件内容, 使用时请注意.
    
Version 1.6.7a5
-------------------

Released: 2018-10-31

	
更新内容:
    
    * 杀作业允许杀队列中的作业
    * 解决作业恢复时无任何反应的bug(jobfilebuild)

Version 1.6.7a4
-------------------

Released: 2018-10-31

	
更新内容:
    
    * 解决作业删除时卡死的bug,
    * 解决杀作业时卡死的bug

Version 1.6.7a3
-------------------

Released: 2018-10-24

	
更新内容:
    
    * 修改作业删除的bug
    * 参数文件中的值允许为特殊字段, 如'\n','\r'

Version 1.6.7a2
-------------------

Released: 2018-10-23

	
更新内容:
    
    * 新增杀作业接口 :py:mod:`jobdelete_rid.do`
    * 参数默认值文件区分大小写

Version 1.6.7a1
-------------------

Released: 2018-10-12

	
更新内容:
    
    * 界面参数文件新增link类型, 用于数据流传递. `参数文件说明 <http://192.168.2.100/mirrorgroup/mirror/wikis/%E7%95%8C%E9%9D%A2%E5%8F%82%E6%95%B0%E6%96%87%E4%BB%B6%E8%AF%B4%E6%98%8E>`_
    * 作业相关服务增加 **kwargs参数
    


Version 1.6.6
-------------------

Released: 2018-09-25

	
更新内容:
    
    * 正式发布1.6.6版本.
    

    
Version 1.6.6rc2
-------------------

Released: 2018-09-15

	
更新内容:
    
    * 解决长时间运行过程监控消失的bug
    * 修复 pika socket104 问题造成的卡核bug
    * 修改结果查看时路径显示不完整的bug.如 ``fluent.cngs`` 会解析为 ``uent.cngs``



Version 1.6.6rc1
-------------------

Released: 2018-09-04

	
更新内容:
    
    * 已经解决了长时间运行时作业不能继续计算的bug ,对应的禅道编号为 ``97`` .(ywx和lyc都这样说)

.. warning::
    
    此版本需要更换python的第三方库, 张文帅更新了Logstash.   `第三方库下载 <http://192.168.2.100/mirrorgroup/mirror/wikis/%E4%BE%9D%E8%B5%96%E8%AF%B4%E6%98%8E>`_

Version 1.6.6b3
-------------------

Released: 2018-08-29

	
更新内容:
    
    * ruok 增加最大jobQueue的字段
    * 修改Ignore参数时不能参数解析list的bug
    * 继续优化大作业计算

Version 1.6.6b2
-------------------

Released: 2018-08-24

	
更新内容:
    
    * 修复autorun不能加载的bug
 

Version 1.6.6b1
-------------------

Released: 2018-08-22

	
解决bug:
    
    * 修改多个计算包适配器混乱的bug, 废弃AddSiteLib函数, 使用ZipImporter加载.
    * 优化了Session超时问题
    * ruok功能新增 Hemiplegia Job字段
    * 解决了作业卡死问题, 作业如果长时间未响应, 会重新触发作业事件. 默认为20次作业监控间隔.
    * 解决了RabbiTMQ Connection Reset BY peer 的bug

新增功能:
    
    * 新增了杀作业接口 :py:mod:`jobkill_rid.do`

    
Version 1.6.6a1
-------------------

Released: 2018-08-16

	
解决bug:
    
    * 解决session超时的bug
    * 解决作业假死问题, 重新加载作业
    * 解决IgnoreMulcase问题, 删除para里面的IgnoreMulcase参数
    * 新增ruok功能
    * 修改资源包加载判断规则.

.. warning::
    
    使用此版本需要修改module.conf的规则RunRoles

Version 1.6.5.3
-------------------

Released: 2018-08-09

	
解决bug:
    
    * 解决getalljob 时startwith的错误 :py:mod:`project.getalljob`
    * 解决session超时问题
    * 修改单状态不能提交作业的bug
    * 修改NCPUS不存在于参数文件不报错的bug

Version 1.6.5.2
-------------------

Released: 2018-08-07

	
新增功能:
    
    * para.xml多状态规则
 
    

Version 1.6.5.1
-------------------

Released: 2018-08-06

	
新增功能:
    
    * 集群集群版本的作业调度接口及外部注入规则
    * para.xml 配置错误时新增判断规则
    * 新增LSF调度器
    
修复bug:
    
    * 修复数据库越界bug


Version 1.6.4.3
-------------------

Released: 2018-08-02

	
	
修改bug:
	
	* 修复多线程访问时, 作业不能继续执行的重大bug

Version 1.6.4.2
-------------------

Released: 2018-07-31

	
	
修改bug:
	
	* 修复数据库高频率访问时的bug
	* AMQP配置作为全局变量来进行配置

Version 1.6.4.1
-------------------

Released: 2018-07-25

新增接口:
	
	* 新增magicfs的relativePath2AbsolutePath接口
	* 新增util中的 tablenamemap 接口
	
	
修改bug:
	
	* 修复 "参数文件中若缺少type字段，后台报错，返回异常"  (#29)
	* 修复 "参数文件中缺少文件参数" (#30)


Version 1.6.4
-----------------

Released: 2018-07-25

新增接口:

    * 新增过程监控接口 :py:mod:`jobprocessmonitor_rid.do`
    * 新增结果回收接口 :py:mod:`jobresultrecovery_rid.do`
    * 获取作业计算数据接口 :py:mod:`jobgetdata.do`
    * 新增获取作业资源机编号接口 :py:mod:`job.getrid`
    * 新增新建工程接口 :py:mod:`project.new`
    * 新增获取工程下的所有作业接口 :py:mod:`project.getalljob`
    
修复bug:
    
    * 解决数据库多进程访问bug(#3)

版本新特性:
    
    * 修改了数据库配置文件"db_durable"字段
    * 新增了配置文件DEBUG->autorun_job字段
    * 新增了日志存取接口及日志查询接口



Version 1.6.3
-----------------

Released: 2018-07-08

* 新增分发作业接口 :py:mod:`jobdispatch.do`
* 新增目录生成接口 :py:mod:`jobdirbuild_rid.do`
* 新增文件生成接口 :py:mod:`jobfilebuild_rid.do`
* 新增作业运行接口 :py:mod:`jobrun_rid.do`
