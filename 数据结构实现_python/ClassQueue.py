# -*- codeing = utf-8 -*-
# @Time : 2022/6/4 18:21
# @Author: Wjie
# @File : ClassQueue.py
# @Software: PyCharm


class queue:

    def __init__(self):
        self.A = []

    def isqueueEmpty(self):
        return self.A == []

    def enqueue(self, value) -> None:
        self.A.insert(0, value)

    def getHead(self):
        return self.A[-1]

    def dequeue(self):
        return self.A.pop()

    def queuesize(self):
        return len(self.A)

    def clear(self):
        while self.A:
            self.A.pop()
