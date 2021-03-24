# 日志查找

1. 查找名为xxxxx.log的文件在什么位置，通过-name指定文件名
    ```shell
     find / -name xxxxx.log
    ```
2. 查找文件名中包含abc和def的文件位置
   ```shell
   find /  -name *abc*def*
   ```
3. 查找docker-compose.yml文件中出现字符443的及其前（-B）、后（-A）、前后各5行（-C）的内容
   ```shell
   grep -C 5 "443" ./docker-compose.yml
   ```

4. 找某程序路径
   ```shell
   whereis file_name
   ```
5. **查找某些文件中包含关键字的记录(重要)**
   ```shell
    grep -rn project_id ga.bi.*
   ```
