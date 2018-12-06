Project 
=============

**工程(project)** : 一个算例的所有资源的集合, 拥有唯一标识, 存在内部实体机数据库结构. 一个工程可以对应多个作业


project表结构:

.. literalinclude:: ../examples/db/project.py


新建工程
-----------------------
            
.. py:function:: project.new(name,desc)

    新建工程.
    
    新建工程需要提供名称后描述, 并返回工程名称及工程路径. 然后用户根据工程路径填充工程文件夹内容.
    
    :param name: 工程名称
    :type name: str
    :param desc: 工程描述
    :type desc: str
    
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     [工程编号,工程ftp全路径]
        -1         执行错误     错误描述
        =======   ==========  ============
        
    :rtype: tuple
    
    rpc调用示例 : 
        .. code-block:: python 
            
            from nameko.standalone.rpc import ClusterRpcProxy     
            config = {
                      'AMQP_URI' : 'amqp://hufei:hufei@127.0.0.1',
                      'rpc_exchange': 'mirror_com'
                      }  
            with ClusterRpcProxy(config,timeout=10) as proxy:
                _return = proxy.project.new(name = 'gocart',desc = 'xxxx')
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/project-new?name=gocart&desc=xxxx
            
    正确返回示例 :
        .. code-block:: python 
            
            (0,[24,"ftp://mirror:mirror@192.168.2.2:2121/projects/b83...495b"])
    
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job is not existed , job : 1"]   


获取工程下的所有作业
-----------------------
            
.. py:function:: project.getalljob(project_id)

    获取作业的资源机编号.

    
    :param project_id: 工程id
    :type project_id: int
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     [job_id1, job_id2]
        -1         执行错误     错误描述
        =======   ==========  ============
        
    :rtype: tuple
    
    rpc调用示例 : 
        .. code-block:: python 
            
            from nameko.standalone.rpc import ClusterRpcProxy     
            config = {
                      'AMQP_URI' : 'amqp://hufei:hufei@127.0.0.1',
                      'rpc_exchange': 'mirror_com'
                      }  
            with ClusterRpcProxy(config,timeout=10) as proxy:
                _return = proxy.project.getalljob(project_id=2)
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/project-getalljob?project_id=2
            
    正确返回示例 :
        .. code-block:: python 
            
            (0,[1,2,3,4,5])
    
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job is not existed , job : 1"]   