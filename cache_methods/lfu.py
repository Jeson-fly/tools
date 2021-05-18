# -*- coding: utf-8 -*-
"""
@Time : 2021/5/17  13:54
@Author : lining
@email：lining01@tuyooganme.com
@desc: LFU最少访问频率算法（小根堆）
"""
import time
import random


class HeapNode(object):
    """
        数据堆的节点
    """

    def __init__(self, data):
        self.index = 0
        self.data = data
        self.use_times = 1

    def __str__(self):
        return str(self.data)

    def __gt__(self, other):
        """大于运算符"""
        return self.use_times > other.use_times

    def __lt__(self, other):
        """小于运算符"""
        return self.use_times < other.use_times

    def destory(self):
        self.data = None
        self.use_times = 1


class EasyHeap(object):
    """
    简单的堆结构，不使用内置的原因是内置堆操作列表事件复杂度为o（N）
    """

    def __init__(self, opacity):
        self.opacity = opacity
        self._heap = [HeapNode(None) for _ in range(opacity)]
        self._size = 0

    def _get_parent(self, index):
        """获取符节点"""
        if index <= 0:
            return None
        parent_index = (index - 1) // 2
        return self._heap[parent_index]

    def _get_left_child(self, index):
        """获取左孩子"""
        left_child_index = 2 * index + 1
        if left_child_index >= self._size:
            return None
        return self._heap[left_child_index]

    def _get_right_child(self, index):
        """获取右孩子"""
        right_child_index = 2 * index + 2
        if right_child_index >= self._size:
            return None
        return self._heap[right_child_index]

    def _heap_fix_up(self, node):
        """节点上升"""
        if not node:
            return
        index = node.index
        parent_node = self._get_parent(index)
        if parent_node and node < parent_node:
            self._exchange_node(node, parent_node)
            self._heap_fix_up(node)

    def _heap_fix_down(self, node):
        """节点下降"""
        if not node:
            return
        index = node.index
        left_child_node = self._get_left_child(index)
        right_child_node = self._get_right_child(index)
        min_node = node if node < left_child_node else left_child_node
        min_node = min_node if min_node < right_child_node else right_child_node
        if min_node is not node:
            self._exchange_node(node, min_node)
            self._heap_fix_down(node)

    def _exchange_node(self, node1, node2):
        """交换两个节点"""
        node1.index, node2.index = node2.index, node1.index
        self._heap[node1.index] = node1
        self._heap[node2.index] = node2

    def heap_fix(self, node):
        """调整节点位置"""
        self._heap_fix_down(node)
        self._heap_fix_up(node)

    def get_head(self):
        """获取头部节点"""
        if self._size <= 0:
            return None
        return self._heap[0]

    def heap_pop(self):
        """推出头部节点"""
        if self._size <= 0:
            return None
        # 交换头尾节点
        head_node = self._heap[0]
        tail_node = self._heap[self._size - 1]
        self._exchange_node(head_node, tail_node)
        self._size -= 1

        # 节点调整
        self.heap_fix(self._heap[0])
        return head_node

    def heap_push(self, node):
        """将节点加入到堆中"""
        node.index = self._size
        self._heap[self._size] = node
        self._size += 1

        # 节点调整
        self.heap_fix(self._heap[self._size - 1])

    def get_size(self):
        """获取堆的尺寸"""
        return self._size

    def show_heap(self):
        """显示整个堆"""
        res = []
        for node in self._heap:
            node and res.append([node.data.get("_key", None), node.use_times, node.index])
        print(res)

    def destory(self):
        """缓存的清空"""
        for node in self._heap:
            node.destory()


class LfuCache(object):
    def __init__(self, cache_time, opacity):
        # 缓存设置
        self._opacity = opacity
        self._dity_time = cache_time

        # 数据缓存内部变量
        self._cache_map = {}  # {key:node}
        self._heap = EasyHeap(self._opacity)

    def get_data(self, key):
        """获取数据"""
        node = self._cache_map.get(key)
        if not node or node.data:
            return None
        time_stamp = node.data.get("_time_stamp")
        if int(time.time()) > time_stamp + self._dity_time:
            return None
        node.use_times += 1
        self._heap.heap_fix(node)
        return node.data

    def push_data(self, key, data):
        """存储数据"""
        assert isinstance(data, dict)

        data.update({"_key": key, "_time_stamp": int(time.time())})
        if key in self._cache_map:
            if self._cache_map[key]:
                self._cache_map[key].data = data
                return
            else:
                self._cache_map.pop(key)

        node = HeapNode(data)
        if self._heap.get_size() >= self._opacity:
            remove_node = self._heap.heap_pop()
            if remove_node and remove_node.data:
                self._cache_map.pop(remove_node.data.get("key"))
        self._heap.heap_push(node)
        self._cache_map.update({key: node})

    def clean_data(self):
        """清除缓存"""
        self._cache_map.clear()
        self._heap.destory()


if __name__ == '__main__':
    cache_obj = LfuCache(5, 10)
    for i in range(10000):
        if random.random() < 0.5:
            key = random.randint(1, 30)
            cache_obj.push_data(key, {"key": key})
        else:
            cache_obj.get_data(random.randint(1, 30))
    cache_obj.clean_data()
