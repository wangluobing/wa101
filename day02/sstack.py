"""
sstack.py  栈模型的顺序存储
重点代码

思路总结：
1. 列表即顺序存储，但功能多，不符合栈的模型特征
2. 利用列表 将其封装，提供接口方法
"""


# 自定义异常
class StackError(Exception):
    pass


# 顺序栈类
class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 列表的最后一个元素作为栈顶
        self._elems = []

    # 判断列表是否为空
    def is_empty(self):
        return self._elems == []

    # 入栈
    def push(self, val):
        self._elems.append(val)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        # 弹出并返回
        return self._elems.pop()

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems[-1]
if __name__ == "__main__":
    st = SStack()  # 初始化栈

    while True:
        syr_input = input()

        if syr_input == int:
            st.push(syr_input)

        elif syr_input == "p":
            st.top()

