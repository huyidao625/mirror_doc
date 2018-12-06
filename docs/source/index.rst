:orphan:

Mirror
======

*[mi-rə]*

.. pull-quote ::

    一款中间件产品，适用于科学计算领域。

A nameko service is just a class:

.. code-block:: python

    # helloworld.py

    from nameko.rpc import rpc

    class GreetingService:
        name = "greeting_service"

        @rpc
        def hello(self, name):
            return "Hello, {}!".format(name)


You can run it in a shell:

.. code-block:: shell

    $ nameko run helloworld
    starting services: greeting_service
    ...

.. note::

    测试Note
    
.. image:: img/faker.png






用户手册
------------------

.. toctree::
    :maxdepth: 2
    
    guide/whatsthemirror.rst
    guide/keyconcepts.rst
    guide/install.rst
    
    


接口说明
----------------

.. toctree::
    :maxdepth: 2
    
    
    ref/job.rst
    ref/project.rst

标准及规范
--------------------

.. toctree::
    :maxdepth: 2
    
    
    standard_com.rst


    
    
版本说明
----------

.. toctree::
    :maxdepth: 2
    
    release.rst