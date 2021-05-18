# mongodb

### 1. CURD

```shell
# 1.增加
db.collection.insert({})
```

```shell
# 2.  删除（delete）
db.collection.remove({})
```

```shell
# 3. 查询（read）
db.collection.find({})
db.collection.find_one({})
```

```shell
# 4. 修改()
db.collection.update({})
```

1. 修改器
    - $set
    - $inc
    - $push
    - $ne 将数组作为数据集使用，保证数组内元素不重复
    - $addToSet

upsert


```mysql
select winner,subject from
(select *, subject in ('physics','chemistry') as new from nobel)
where yr=1984
order by new desc,subject,yr
```