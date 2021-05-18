# -*- coding: utf-8 -*-
"""
@Time : 2021/5/12  09:35
@Author : lining
@email：lining01@tuyooganme.com
@desc: LRU (least recently used)
        最近访问最少算法
"""

from tools.data_structure.double_link_list import DoubleLinkList, ListNode
import time


class LRUCache(object):
    def __init__(self, cache_time, opacity):
        # 缓存参数设置
        self._cache_time = cache_time
        self._opacity = opacity

        # 缓存变量
        self._data_map = {}
        self._double_link_list = DoubleLinkList()

    def push_data(self, key, data):
        """数据存储"""
        assert isinstance(data, dict)
        data.update({"_ts": int(time.time()), "_key": key})
        if key in self._data_map:
            if self._data_map[key]:
                self._data_map[key].data = data
                return
            else:
                self._data_map.pop(key, 0)

        # 将数据插入到双端队列头部
        node = ListNode(data)
        if self._double_link_list.get_size() >= self._opacity:
            remove_node = self._double_link_list.pop_back()
            if remove_node and remove_node.date:
                self._data_map.pop(remove_node.date.get("_key"))
        self._double_link_list.push_front(node)
        self._data_map[key] = node

    def get_data(self, key):
        """获取数据"""
        node = self._data_map.get(key)
        if not node or not node.data:
            return None
        time_stamp = node.data.get("_ts")
        if time.time() - self._cache_time < time_stamp:
            self._double_link_list.remove_node(node)
            self._double_link_list.push_front(node)
            return node.data
        else:
            return None

    def destory(self):
        """清空缓存"""
        self._data_map.clear()
        self._double_link_list.destory()
