# 分布式锁

## 分类
1. 处理程序是单进程多线程的，在python下，就可以使用threading模块的Lock
   对象来限制对共享变量的同步访问，实现线程安全；
   
2. 单机多进程，在python下。可以使用multiprocessing的Lock对象处理

3. 多机多进程部署的情况下，就得依赖一个第三方组件（存储锁对象）来实现一个
   分布式的同步锁了
   

## 分布式锁实现方式
1. 基于数据库来实现，如mysql；
    - 基于数据库表
    - 基于数据库排它suo

2. 基于缓存来实现，如redis；

3. 基于zookeeper来实现


