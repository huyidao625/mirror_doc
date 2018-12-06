前后台接口规范
====================

通信协议
----------

约定采用 ``AMQP1.0(ISO/IEC 19464)`` 为标准通信协议.


数据交换格式
-------------

约定采用 ``json(ECMA-404)`` 作为前后端数据标准交换格式 . 

.. note::

    本文档中的所有关于Json的名词都从此文档中引用. 文档为 ``ECMA-404.pdf``


功能接口标准
--------------

约定提供 ``RPC`` 调用及 ``HTTP`` 代理调用接口

RPC调用语法为:

    .. code-block:: python 
    
        rpc.servicename.servicemethod(parameters)
    
示例如下:
    
    .. code-block:: python
        
        rpc.job.run(job_id='1')

HTTP代理调用语法为:

    .. code-block:: html 
    
        http://ip:port/proxy/servicename-servicemethod?parameters

示例如下:
        
    .. code-block:: html 
    
        http://192.168.2.2/proxy/job-run?job_id=1
    
返回值约定
----------------

为了前后端的处理方便, 故约定返回值标准如下:
    
1. 返回值必须是一个可序列化为 ``Json Arrays`` 的对象. 只包含两部分, 第一部分是状态码( ``returncode`` ) ,第二部分是返回内容( ``content`` ). 状态码必须可序列化为 ``Json Numbers`` .  返回内容必须是可进行Json序列化的对象 , 比如 ``Json Array`` , ``Json Numbers`` , ``Json String`` , ``Json Values`` , ``Json Objects`` . 

    如下所示:
        
        .. code-block:: python
        
            [ 0 , [1,2,3,4,5]]
        
        或者
        
        .. code-block:: python
            
            [-1 , "input , error"]
        
        或者
        
        .. code-block:: python
        
            [0 , {"process":
                    {"current_step":9, 
                    "all_step":10 ,
                    "info":"ftp://192.168.2.8/Jobs/1234/info"
                    }
                 }
            ]

2. 约定状态码( ``returncode`` ) 为 ``0`` 时 , 代表正确执行 , 返回内容( ``content`` ) 则为返回的内容.

3. 约定状态码( ``returncode`` ) 为 ``非0`` 时 , 代表执行错误 , 返回内容( ``content`` ) 为一个 ``Json String`` , 表示错误描述.
    
    


通知及回调接口约定
---------------------

文件传输协议约定
----------------------