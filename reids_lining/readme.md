# redis原理解析

### 一、基本数据结构

    1 简单动态字符串（SDS：simple dynamic string）
    2 链表
    3 字典
    4 跳跃表
    5 整数集合
    6 压缩列表
    7 对象（5种数据结构、内存回收、对象共享）

### 二、单机数据库

    1 数据库
    2 RDB 持久化
    3 AOF 持久化
    4 事件
    5 客户端
    6 服务器

### 三、多机数据库

    1 复制（主从复制）
    2 哨兵（sentinel）
    3 集群（cluster）

### 四、独立功能

    1 订阅和发布功能
    2 事物操作
    3 lua脚本支持
    4 排序
    5 二进制位数组
    6 慢查询日志
    7 监视器
***
1. 主从复制
   - psync、sync

***
### 发布和订阅
1. 基本命令 
   - PUBLIST  想频道推送消息
   - SUBSCRIBE/UNSUBCRIBE 订阅/退订频道
   - PSUBSCRIBE/PUNSUBCRIBE 订阅/退订模式
   - PUBSUB CHANNELS 查看频道 
   - PUBSUB NUMPAT 查看订阅的模式数量
   ```shell
   # 向某个频道推送消息：publist 频道 消息
      publish new-it success
   # 订阅/退订频道： subscribe 频道名称(一个或多个)  包含该频道就将订阅者加入到该频道链表的最后，不包含该频道，则创建
      subscribe new-it new-sport
      unsubscribe new-it new-sport
   # 订阅/退订模式：psubscribe 模式名称
      psubscribe new-it new-sport
      punsubscribe new-it new-sport
   # 查看频道信息
      subpub channels
   # 查看模式数量
      subpub numpat 
   ```
   
2. 发布订阅分为频道和模式，客户端可以订阅和去掉订阅某一个频道，也可以订阅和取消订阅某一个模式，模式是一些频道的集合。
加入用户订阅的某个频道，当该频道有消息进来时，客户端就能收到此消息，订阅了相关模式也同理。频道和模式都存储在redisServer
   字典中，pubsub_channel属性存储频道相关，pubsub_patterns属性存储模式相关。频道中键是频道的名称，值是一个链表；
   模式是一个链表，每个节点是一个pubsubPattern（{"client":...,"pattern":...}）
***

### 事务

1. 四大原则
    - 原子性（atomic）要么执行所有的操作，要么就一个操作也不执行
    - 一致性（consistency）数据库在执行事物之前是一致的，在执行事物之后也是一致的
    - 隔离性（Isolation）不同事务之间不会产生相互影响
    - 持久性（durability） 在RDB或AOF模式下才具有此特性

2. 基础命令
    - MULIT、EXEC、WATCH（监视某个健）

***

### 二进制位数组

1. 基础命令
   - SETBIT
   - GETBIT
   - BITCOUNT时间复杂度 O(n)
   - BITOP（逻辑或｜、逻辑与&、逻辑非~、逻辑异或^）
   ```shell
   # 
   ```

2. BITCOUNT的三种实现
    - 遍历
    - 查表法
    - swar方法（计算汉明重量）
    - redis中采用第二种和第三种组合的方式来实现
3. redis使用SDS保存位数组，并按照逆序的形式存储，这样主要是为了易于空间扩展
***
### 监视器
1. monitor让一个客户端成为监视器 实时的接收并打印服务器处理的命令请求
   ```shell
    MONITOR
   ```
***
### 慢查询日志
1. 参数
   - slow-log-slower-than 数值  执行时间超过多少秒的记录到慢查询日志 
   - slowlog-max-len 数值服务器最多保存多少调慢查询日志


