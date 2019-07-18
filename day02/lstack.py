"""
lstack.py  栈的链式栈
重点代码

思路分析：
1. 源于链表结构
2. 封装栈的操作方法（入栈，出栈，栈空，栈顶元素）
3. 链表的开头作为栈顶 ？ （不用每次遍历）
"""

# 自定义异常
class StackError(Exception):
    pass

# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 链式栈操作
class LStack:
    def __init__(self):
        # 标记栈的栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self,val):
        self._top = Node(val,self._top)

    def pop(self):
        if self._top is None:
            raise StackError("Stack is emtpy")
        value = self._top.val
        self._top = self._top.next
        return value
    def top(self):
        if self._top is None:
            raise StackError("Stack is emtpy")
        return self._top.val

if __name__ == "__main__":
    ls = LStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    print(ls.pop())
    print(ls.pop())