# -*- coding: utf-8 -*-
"""
@Time : 2021/5/11  18:45
@Author : lining
@email：lining01@tuyooganme.com
@desc: FIFO(first in first out)先进先出
"""
import time, random


class FIFOCache(object):
    """数据缓存类，使用FIFO算法，设置过期时间戳"""

    def __init__(self, cache_time, opacity):
        self.cache_time = cache_time
        self.opacity = opacity
        self._index = 0
        self._key_list = [None for _ in range(self.opacity)]
        self._cache_date = {}

    def push_data(self, key, data):
        """数据加入缓存"""
        if not isinstance(data, dict):
            return None
        data.update({"_time_stamp": int(time.time())})
        if key in self._cache_date:
            self._cache_date[key] = data
            return
        if self._index >= self.opacity:
            self._index = 0
        # 删除旧数据
        old_key = self._key_list[self._index]
        if old_key:
            self._cache_date.pop(old_key)
        self._cache_date[key] = data

        # 索引递增
        self._key_list[self._index] = key
        self._index += 1

    def get_data(self, key):
        """获取数据"""
        data = self._cache_date.get(key, None)
        time_stamp = data.get("_time_stamp", 0)
        if time.time() - time_stamp < self.cache_time:
            return data
        else:
            return None

    def clean_cache(self):
        """缓存销毁"""
        self._cache_date.clear()
        self._key_list = []


if __name__ == '__main__':
    cache_obj = FIFOCache(1, 10)
    for i in range(50):
        key = random.randint(1, 15)
        print(key, i)
        cache_obj.push_data(key, {"key": key})
        print("+++", cache_obj._key_list)
        print("----", cache_obj._cache_date)
