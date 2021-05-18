# -*- coding: utf-8 -*-
"""
@Time : 2021/5/13  13:13
@Author : lining
@email：lining01@tuyooganme.com
@desc:  双端链表
"""


class ListNode(object):
    def __init__(self, data=None):
        self.pre_node = None
        self.next_node = None
        self.date = data

    def clean_pointer(self):
        """清空指针，避免不必要的连接错误"""
        self.pre_node = None
        self.next_node = None

    def destory(self):
        """节点销毁"""
        self.clean_pointer()
        self.date = None


class DoubleLinkList(object):
    def __init__(self):
        """初始化"""
        self._head_node = ListNode()
        self._tail_node = ListNode()
        self._head_node.next_node = self._tail_node
        self._tail_node.pre_node = self._head_node
        self.size = 0

    def _insert_data(self, node: ListNode, pre_node: ListNode, next_node: ListNode):
        """插入节点"""
        node.clean_pointer()
        pre_node.next_node = node
        node.pre_node = pre_node
        next_node.pre_node = node
        node.next_node = next_node
        self.size += 1

    def _remove_data(self, node: ListNode):
        """删除数据"""
        if node is self._head_node or node is self._tail_node:
            return
        if node.pre_node is not self._head_node:
            node.pre_node.next_node = node.next_node
        if node.next_node is not self._tail_node:
            node.next_node.pre_node = node.pre_node
        node.clean_pointer()
        self.size -= 1
        return node

    def push_front(self, node):
        """队首添加数据,时间复杂度O(1)"""
        assert isinstance(node, ListNode)
        self._insert_data(node, self._head_node, self._head_node.next_node)

    def push_back(self, node):
        """队尾添加元素,时间复杂度O(1)"""
        assert isinstance(node, ListNode)
        self._insert_data(node, self._tail_node, self._tail_node.pre_node)

    def pop_front(self):
        """弹出队首元素,时间复杂度O(1)"""
        return self._remove_data(self._head_node.next_node)

    def remove_node(self, node):
        """移除指定节点"""
        assert isinstance(node, ListNode)
        self._remove_data(node)

    def pop_back(self):
        """弹出队尾元素"""
        return self._remove_data(self._tail_node.pre_node)

    def get_head(self):
        """获取队首元素"""
        if self._head_node.next_node is self._tail_node:
            return None
        return self._head_node.next_node

    def get_back(self):
        """获取队尾元素"""
        if self._tail_node.pre_node is self._head_node:
            return None
        return self._tail_node.pre_node

    def get_size(self):
        """获取链表长度"""
        return self.size

    def clear_node(self):
        """清除链表节点"""
        next_node = self._head_node.next_node
        while next_node:
            tmp_node = next_node.next_node
            next_node.destory()
            next_node = tmp_node
        self._head_node.next_node = self._tail_node
        self._tail_node.pre_node = self._head_node
        self.size = 0

    def destory(self):
        """链表的销毁"""
        self.clear_node()
        self._head_node and self._head_node.destory()
        self._tail_node and self._tail_node.destory()
