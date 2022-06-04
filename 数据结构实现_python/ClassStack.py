# -*- codeing = utf-8 -*-
# @Time : 2022/6/4 18:19
# @Author: Wjie
# @File : ClassStack.py
# @Software: PyCharm


class Stack:

    def __init__(self):
        self.A = []

    def isstackEmpty(self):
        return self.A == []

    def push(self, value) -> None:
        self.A.append(value)

    def pop(self):
        return self.A.pop()

    def stacksize(self):
        return len(self.A)

    def clear(self):
        while self.A:
            self.A.pop()
