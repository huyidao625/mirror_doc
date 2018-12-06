安装Mirror
================

概述
-----------------

Mirror1.6 用到了一些新的框架和库, 包括MySQL数据库服务器, RabbitMQ消息队列服务器, Zookeeper分布式日志协调服务器. 

安装MySQL服务器
-----------------

Mysql服务器硬件要求:
    
    * 4G运行内存
    * 50G磁盘空间
    * 2G Hz CPU主频
    * 100M带宽网络

Mysql服务器版本要求:
    
    * 必须大于Mysql5.7版本
    * 最好采用8.0版本

Windows安装及配置
^^^^^^^^^^^^^^^^^^^^

安装: 略

必须的配置: 默认配置即可


Linux安装及配置
^^^^^^^^^^^^^^^^^^^^

安装: 略

必须的配置: 默认配置即可 



安装RabbitMQ服务器
--------------------

Windows安装及配置
^^^^^^^^^^^^^^^^^^^^

安装: 略

必须的配置: 默认配置即可

Linux安装及配置
^^^^^^^^^^^^^^^^^^^^

安装: 略

必须的配置: 默认配置即可

安装Zookeeper服务器
---------------------

以安装 ``zookeeper 3.4.10`` 为例.

第一步: 解压

tar zxvf   zookeeper-3.4.10.tar.gz
cd zookeeper-3.4.10/
cp conf/zoo_sample.cfg  conf/zoo.cfg
vi conf/zoo.cfg


```
# The number of milliseconds of each tick
tickTime=2000
# The number of ticks that the initial 
# synchronization phase can take
initLimit=10
# The number of ticks that can pass between 
# sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just 
# example sakes.
dataDir=/home/lyc/soft/zookeeper-3.4.10/data
# the port at which the clients will connect
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
#
# Be sure to read the maintenance section of the 
# administrator guide before turning on autopurge.
#
# http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
#
# The number of snapshots to retain in dataDir
#autopurge.snapRetainCount=3
# Purge task interval in hours
# Set to "0" to disable auto purge feature
#autopurge.purgeInterval=1

```



更改配置文件名称：mv zoo_sample.cfg  zoo.cfg

其它参数为默认

```
设置环境变量： vi ~/.bashrc 

PATH=/home/lyc/app/ansys/ansys_inc/v160/fluent/bin:/home/lyc/soft/python3/bin:/home/lyc/soft/python/bin:/home/lyc/soft/jdk1.8.0_144/bin:/home/lyc/soft/zookeeper-3.4.10/bin:$PATH
export PATH
export LD_LIBRARY_PATH=/home/lyc/soft/mpich2/lib:$LD_LIBRARY_PATH
```

配置完成后，source ~/.bashrc

启动 zookeeper : 进入到bin目录下，./zkServer.sh start ,若出现如下

```
[lyc@localhost bin]$ ./zkServer.sh start 
ZooKeeper JMX enabled by default
Using config: /home/lyc/soft/zookeeper-3.4.10/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
```

则表示zookeeper启动成功



安装日志服务器
---------------------

Mirror服务器安装
---------------------




