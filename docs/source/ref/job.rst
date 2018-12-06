Job 
=============

**作业(job)** : 一个确定了输入的计算状态, 有固定的运行目录, 并且具备监控和回收的特征. 可以直接运行或经调度后运行的实体.

**计算步骤(step)** : 通常一个作业都会有多个exe, 执行时按照一定规律进行执行, 比如: 并行多核解算器计算时可以分为 网格剖分, 解算器运行, 流场合并等步骤, 每个步骤都以独立的exe和提交格式 , mirror中把类似这样的步骤称为mirror的计算步骤.

下面是一个适配器中的计算步骤模板:
    
.. code-block:: python
 
    <ExeArgument id="grid" type="shell" value="PiGrid_APP.exe" workpath="GRID" priority="1" postmethod="gridPost" premethod="gridPre"></ExeArgument>
    <ExeArgument id="flow" type="shell" value="PF_App.exe" workpath="FLOW" priority="2" postmethod="flowPost"></ExeArgument>
    <ExeArgument id="post" type="shell" value="python PiPost.py" workpath="POST" priority="3"></ExeArgument>
            
            

一个作业的完整运行周期为:   

    1. 作业分发 :py:mod:`jobdispatch.do`
    2. 目录生成 :py:mod:`jobdirbuild_rid.do`
    3. 文件生成 :py:mod:`jobfilebuild_rid.do`
    4. 提交运行 :py:mod:`jobrun_rid.do`
    5. 过程监控 :py:mod:`jobprocessmonitor_rid.do`
    6. 结果回收 :py:mod:`jobresultrecovery_rid.do`
    7. 查看结果 :py:mod:`jobgetdata.do`

job表结构:

.. literalinclude:: ../examples/db/job.py


作业分发
----------------
            
.. py:function:: jobdispatch.do(p_id,c_id,para_name=para.xml)

    分发作业。

    把工程拆按照多状态规则拆分为作业。同时把作业加入到作业表中，并把作业id加入到rabbit的相应queue中。
    
    .. warning::
        如果资源机配置为作业自动运行, 即配置文件 ``DEBUG->autorun_job == true``. 则资源机会自动的进行作业的目录生成, 文件生成 , 计算, 结果回收. 不需要手动的去调用作业的每一步.
        
    :param p_id: 工程id
    :type p_id: int
    :param c_id: 计算包id
    :type c_id: int
    :param para_name: 参数文件名称。默认为：para.xml
    :type para_name: str
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     []
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
                _return = proxy.jobdispatch.do(p_id=2,c_id=1,para_name='piflow.xml')
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/jobdispatch-do?p_id=2&c_id=1&para_name=piflow.xml
    
    正确返回:
        
        .. code-block:: shell
        
            [0 , []]
            
    错误返回:
        
        .. code-block:: shell
        
            [-1,"calcpackage is not existed , calcpackage : 1"]
        
    
    .. note::
        
        同一个工程可以多次进行作业分发, 产生相同的作业.

    
作业目录生成
----------------
            
.. py:function:: jobdirbuild_rid.do(job_id, force=0)

    手动生成作业目录, 下载相关文件, 并且解压出计算包中的软件目录.

    手动的进行作业目录生成. 包括生成运行目录, 下载计算包文件到 ``.mirror/calc`` , 下载工程文件到 ``.mirror/proj`` ,  解压计算包的 ``template`` 到作业目录主目录.
    
    .. warning:: 
        此接口为动态接口. 需要使用到 ``rid`` ,即资源机id. 用户需要先通过接口 :py:func:`job.getrid` 查询到作业的资源机id.  如:查询到的rid为5, 则此接口为 ``jobdirbuild_5.do(job_id, force=0)``
    
    :param job_id: 作业id
    :type p_id: int
    :param force: 是否强制进行目录生成.默认为0, 0-不强制生成, 1-强制生成.
        
    .. warning::
        当force = 1时, 强制进行目录生成会重新建一个目录, 且不会保存上一个已经存在的作业目录, 也不会删除前一个目录. job表中的path会直接指向新的目录地址
        
    :type force: int
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     []
        -1         执行错误     错误描述
        =======   ==========  ============
        
    :rtype: list
    
    
    rpc调用示例 : 
        .. code-block:: python 
            
            from nameko.standalone.rpc import ClusterRpcProxy     
            config = {
                      'AMQP_URI' : 'amqp://hufei:hufei@127.0.0.1',
                      'rpc_exchange': 'mirror_com'
                      }  
            with ClusterRpcProxy(config,timeout=10) as proxy:
                _return = proxy.jobdirbuild_5.do(job_id=1,force=0)
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/jobdirbuild_5-do?job_id=1&force=0
    
    正确返回:
        
        .. code-block:: shell
        
            [0 , []]
            
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job is not existed , job : 1"]
    
    .. note::
    
        如果资源机配置为作业自动运行, 即配置文件 ``DEBUG->autorun_job == true``. 则资源机会自动的进行作业的目录生成, 文件生成 , 计算, 结果回收. 自动运行时不需要手动调用此接口. 
        
    .. note::
    
        如果需要进行重新计算, 或者手动调试时, 可以关闭自动运行作业. 然后手动的运行此接口.
        
作业文件生成
----------------
            
.. py:function:: jobfilebuild_rid.do(job_id)

    手动生成作业文件.

    手动的生成作业所需的相关文件, 如参数文件. 包括生成参数文件, 拷贝文件. 即根据拷贝规则 ``<File name="{model}" target="GRID/{model}" create="1" unzip="0" />`` 进行相应拷贝. 
    
    .. warning:: 
    
        此接口为动态接口. 需要使用到 ``rid`` ,即资源机id. 用户需要先通过接口 :py:func:`job.getrid` 查询到作业的资源机id.  如:查询到的rid为5, 则此接口为 ``jobfilebuild_5.do(job_id)``
    
    :param job_id: 作业id
    :type p_id: int
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     []
        -1         执行错误     错误描述
        =======   ==========  ============
        
    :rtype: list
    
    
    rpc调用示例 : 
        .. code-block:: python 
            
            from nameko.standalone.rpc import ClusterRpcProxy     
            config = {
                      'AMQP_URI' : 'amqp://hufei:hufei@127.0.0.1',
                      'rpc_exchange': 'mirror_com'
                      }  
            with ClusterRpcProxy(config,timeout=10) as proxy:
                _return = proxy.jobfilebuild_5.do(job_id=1)
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/jobfilebuild_5-do?job_id=1

    正确返回:
        
        .. code-block:: shell
        
            [0 , []]
            
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job is not existed , job : 1"]
            
    .. note::
    
        如果资源机配置为作业自动运行, 即配置文件 ``DEBUG->autorun_job == true``. 则资源机会自动的进行作业的目录生成, 文件生成 , 计算, 结果回收. 自动运行时不需要手动调用此接口. 
        
    .. note::
        
        此接口会重新取job表的para参数进行文件生成, 即可以修改数据库的参数, 然后再运行此接口 ,重新生成参数文件.

作业运行
----------------
            
.. py:function:: jobrun_rid.do(job_id,step=None)

    手动运行作业.

    手动的运行作业, 如果计算步骤step为None或者不传入, 则自动的运行优先级最高的计算步骤.  ``注意: 手动运行作业时必须全手动的运行作业步骤``.
    
    .. warning:: 
    
        此接口为动态接口. 需要使用到 ``rid`` ,即资源机id. 用户需要先通过接口 :py:func:`job.getrid` 查询到作业的资源机id.  如:查询到的rid为5, 则此接口为 ``jobrun_5.do(job_id)``
    
    :param job_id: 作业id
    :type job_id: int
    :param step: 作业计算步骤
    :type step: str
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     []
        -1         执行错误     错误描述
        =======   ==========  ============
        
    :rtype: list
    
    
    rpc调用示例 : 
        .. code-block:: python 
            
            from nameko.standalone.rpc import ClusterRpcProxy     
            config = {
                      'AMQP_URI' : 'amqp://hufei:hufei@127.0.0.1',
                      'rpc_exchange': 'mirror_com'
                      }  
            with ClusterRpcProxy(config,timeout=10) as proxy:
                _return = proxy.jobrun_5.do(job_id=1, step='grid')
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/jobrun_5-do?job_id=1&step=grid

    正确返回:
        
        .. code-block:: shell
        
            [0 , []]
            
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job is not existed , job : 1"]
            
    .. note::
    
        如果资源机配置为作业自动运行, 即配置文件 ``DEBUG->autorun_job == true``. 则资源机会自动的进行作业的目录生成, 文件生成 , 计算, 结果回收. 自动运行时不需要手动调用此接口. 
        
    .. note::
        
        todo : 手动运行作业时, 计算步骤的后置脚本目前不能运行. 手动运行作业时, 目前不会按照计算步骤顺序自动运行完成所有步骤.

作业监控
----------------
            
.. py:function:: jobprocessmonitor_rid.do(job_id)

    手动进行作业监控.

    
    .. warning:: 
    
        此接口为动态接口. 需要使用到 ``rid`` ,即资源机id. 用户需要先通过接口 :py:func:`job.getrid` 查询到作业的资源机id.  如:查询到的rid为5, 则此接口为 ``jobprocessmonitor_5.do(job_id)``
    
    :param job_id: 作业id
    :type job_id: int
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     []
        -1         执行错误     错误描述
        =======   ==========  ============
        
    :rtype: list
    
    
    rpc调用示例 : 
        .. code-block:: python 
            
            from nameko.standalone.rpc import ClusterRpcProxy     
            config = {
                      'AMQP_URI' : 'amqp://hufei:hufei@127.0.0.1',
                      'rpc_exchange': 'mirror_com'
                      }  
            with ClusterRpcProxy(config,timeout=10) as proxy:
                _return = proxy.jobprocessmonitor_5.do(job_id=1)
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/jobprocessmonitor_5-do?job_id=1

    正确返回:
        
        .. code-block:: shell
        
            [0 , []]
            
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job is not existed , job : 1"]
    
    .. note::
    
        如果资源机配置为作业自动运行, 即配置文件 ``DEBUG->autorun_job == true``. 则资源机会自动的进行作业的目录生成, 文件生成 , 计算, 结果回收. 自动运行时不需要手动调用此接口. 
        
        
作业回收
----------------
            
.. py:function:: jobresultrecovery_rid.do(job_id)

    手动进行作业结果回收.
    
    .. warning:: 
    
        此接口为动态接口. 需要使用到 ``rid`` ,即资源机id. 用户需要先通过接口 :py:func:`job.getrid` 查询到作业的资源机id.  如:查询到的rid为5, 则此接口为 ``jobresultrecovery_5.do(job_id)``
    
    :param job_id: 作业id
    :type job_id: int
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     []
        -1         执行错误     错误描述
        =======   ==========  ============
        
    :rtype: list
    
    
    rpc调用示例 : 
        .. code-block:: python 
            
            from nameko.standalone.rpc import ClusterRpcProxy     
            config = {
                      'AMQP_URI' : 'amqp://hufei:hufei@127.0.0.1',
                      'rpc_exchange': 'mirror_com'
                      }  
            with ClusterRpcProxy(config,timeout=10) as proxy:
                _return = proxy.jobresultrecovery_5.do(job_id=1)
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/jobresultrecovery_5-do?job_id=1

    正确返回:
        
        .. code-block:: shell
        
            [0 , []]
            
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job is not existed , job : 1"]            
    
    .. note::
    
        如果资源机配置为作业自动运行, 即配置文件 ``DEBUG->autorun_job == true``. 则资源机会自动的进行作业的目录生成, 文件生成 , 计算, 结果回收. 自动运行时不需要手动调用此接口. 
        

获取作业计算数据
---------------------
            
.. py:function:: jobgetdata.do(job_id)

    获取作业计算数据, 包括过程监控数据和结果数据

    
    :param job_id: 作业id
    :type job_id: int
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     {'process':{过程数据},'result':{结果数据}}
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
                _return = proxy.jobgetdata.do(job_id=2)
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/jobgetdata-do?job_id=1
            
    正确返回示例 :
    
        .. code-block:: python 
            
            [0 , {
                  "process": {
                    "currentstep": "9",
                    "allstep": "10",
                    "gridinfo": "ftp://mirror:mirror@192.168.2.2:2121/job/.../grid",
                    "info": "ftp://mirror:mirror@192.168.2.2:2121/jobs/f24.../flow",
                    "chart": "ftp://mirror:mirror@192.168.2.2:2121/jobs/f/RMSmr.txt"
                               },
                  "result": {
                    "mesh": "ftp://mirror:mirror@192.168.2.2:2121/jobs/f24/MeshTot.dat",
                    "force": "ftp://mirror:mirror@192.168.2.2:2121/jobs/f2/RMSmitor.txt"
                            }
                    }
             ]
             
    正确返回时的返回内容数据结构:
    
        .. code-block:: python
            
            [0 , {
                  "process": {
                            "key":value
                               },
                  "result": {
                            "key":value
                            }
                    }
             ]
    
        错误返回:
        
        .. code-block:: shell
        
            [-1,"job is not existed , job : 1"]            
            
    .. note::
        
       返回内容中 ``process`` 和 ``result`` 是固定的.
       +
       
获取作业资源机编号
---------------------
            
.. py:function:: job.getrid(job_id)

    获取作业的资源机编号.

    
    :param job_id: 作业id
    :type job_id: int
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     resourcemachine_id
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
                _return = proxy.job.getrid(job_id=2)
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/job-getrid?job_id=2
            
    正确返回示例 :
        .. code-block:: python 
            
            [0, 6]
            
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job is not existed , job : 1"]            

            
杀作业
---------------------
            
.. py:function:: jobkill_rid.do(job_id)

        杀作业接口, 停止正在计算的作业 , 并且不进行结果回收.

    
    .. warning:: 
    
        此接口为动态接口. 需要使用到 ``rid`` ,即资源机id. 用户需要先通过接口 :py:func:`job.getrid` 查询到作业的资源机id.  如:查询到的rid为5, 则此接口为 ``jobprocessmonitor_5.do(job_id)``
    
    :param job_id: 作业id
    :type job_id: int
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     []
        -1         执行错误     错误描述
        =======   ==========  ============
        
    :rtype: list
    
    
    rpc调用示例 : 
        .. code-block:: python 
            
            from nameko.standalone.rpc import ClusterRpcProxy     
            config = {
                      'AMQP_URI' : 'amqp://hufei:hufei@127.0.0.1',
                      'rpc_exchange': 'mirror_com'
                      }  
            with ClusterRpcProxy(config,timeout=10) as proxy:
                _return = proxy.jobkill_5.do(job_id=1)
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/jobkill_5-do?job_id=1

    正确返回:
        
        .. code-block:: shell
        
            [0 , []]
            
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job not running , jobid : 1"]
    
    .. warning::
        
        杀作业后不会进行结果回收. 
        
删除作业
---------------------
            
.. py:function:: jobdelete_rid.do(job_id)

        删除作业接口, 删除作业相关数据,包括数据库,作业运行文件夹, 可进行强制删除. 

    
    .. warning:: 
    
        此接口为动态接口. 需要使用到 ``rid`` ,即资源机id. 用户需要先通过接口 :py:func:`job.getrid` 查询到作业的资源机id.  如:查询到的rid为5, 则此接口为 ``jobprocessmonitor_5.do(job_id)``
    
    .. warning::
        
        删除数据为真实的删除数据库中表数据.
    
    :param job_id: 作业id
    :type job_id: int
    :return: 
        
        =======   ==========  ============
        状态码      说明           值
        =======   ==========  ============
        0          执行正确     []
        -1         执行错误     错误描述
        =======   ==========  ============
        
    :rtype: list
    
    :param force: 是否强制删除. 0 代表不强制删除, 1 代表强制删除. 默认为0.
    
    
    rpc调用示例 : 
        .. code-block:: python 
            
            from nameko.standalone.rpc import ClusterRpcProxy     
            config = {
                      'AMQP_URI' : 'amqp://hufei:hufei@127.0.0.1',
                      'rpc_exchange': 'mirror_com'
                      }  
            with ClusterRpcProxy(config,timeout=10) as proxy:
                _return = proxy.jobdelete_5.do(job_id=1,force=1)
                print(_return)
    
    http调用示例 :
        .. code-block:: shell 
            
            http://192.168.2.2:8000/proxy/jobdelete_5-do?job_id=1&force=1

    正确返回:
        
        .. code-block:: shell
        
            [0 , []]
            
    错误返回:
        
        .. code-block:: shell
        
            [-1,"job not running , jobid : 1"]
    
