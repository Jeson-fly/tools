# -*- coding: utf-8 -*-
"""
@Time : 2021/5/17  13:57
@Author : lining
@email：lining01@tuyooganme.com
@desc:  堆节点
"""


class HeapNode(object):
    """
        数据堆的节点
    """

    def __init__(self, data):
        self.index = 0
        self.data = data
        self.use_times = 1

