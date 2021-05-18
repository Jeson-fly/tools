# nodejs
> author : lining
> email: 993811091@qq.com

## 安装
1. win10安装
    - 安装后自动配置到环境变量
    - 查看版本号：```node -v / npm -v ```


10. 修改全局模块路径和缓存路径（可选，大家自行选择是否修改）
当我们在执行npm install express -g命令时，g表示global全局。会默认下载到c盘，c盘一般作为系统盘，尽量把一些程序安装到其他盘，来减少c盘空间的占用

它的默认路径为：【C:\Users\用户名\AppData\Roaming\npm】。

注意：此文件夹默认是隐藏的，需要设置显示隐藏的文件夹，在"查看"菜单中设置，如下图：

这里将全局模块（文件夹名：node_global）和缓存（文件夹名：node_cache）放在了nodejs安装目录下，在你的nodejs安装目录下创建创建两个文件夹，名称分别为：node_global和node_cache，在node_global文件夹下再建一个node_modules文件夹，配置环境变量用


此时，还没有更改完成，需要手动指定到这两个文件夹中
第一种方法：win+R打开运行窗口，输入cmd，再输入以下两条指令
npm config set prefix "创建的node_global文件夹所在路径"
npm config set cache "创建的node_cache文件夹所在路径"
1
2
如：
npm config set prefix "E:\develop\nodejs\node_global"
npm config set cache "E:\develop\nodejs\node_cache"
1
2
3
第二种方法：在nodejs的安装目录下，进入node_modules——>npm——>找到npmrc文件，打开
添加以下命令：
prefix=创建的node_global文件夹所在路径
cache=创建的node_cache文件夹所在路径
如：
prefix=E:\develop\nodejs\node_global
cache=E:\develop\nodejs\node_cache
1
2
3
4
5
6
修改完毕后，再配置环境变量
右键此电脑——>高级系统设置——>环境变量
在系统变量中，新建，变量名：NODE_PATH 变量值：node_global文件夹下的node_modules文件夹。如：E:\develop\nodejs\node_global\node_modules
修改用户变量中的Path变量，将默认的npm路径修改为新建的node_global路径
blog.csdn.net/Small_Yogurt/article/details/104968169