"""
linklist.py
功能：　实现单链表的构建和功能操作
重点代码
"""


# 　创建节点类
class Node:
    """
    思路：　将自定义的类视为节点的生成类，实例对象中
    　　　　包含数据部分和指向下一个节点的ｎｅｘｔ
    """

    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 循环下一个节点关系


#　做链表操作
class LinkList:
    """
    思路：　单链表类，生成对象可以进行增删改查操作
    　　　　具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
        初始化链表，标记一个链表的开端，以便于获取后续
        的节点
        """
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        p = self.head  # p 作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next  # ｐ向后移动

    # 判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 　尾部插入
    def append(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 　头部插入
    def head_insert(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 　指定插入位置
    def insert(self, index, val):
        p = self.head
        for i in range(index):
            # 超出位置最大范围结束循环
            if p.next is None:
                break
            p = p.next

        node = Node(val)
        node.next = p.next
        p.next = node

    # 　删除节点
    def delete(self, x):
        p = self.head
        # 　结束循环必然两个条件其一为假
        while p.next and p.next.val != x:
            p = p.next

        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next

    #　获取某个节点值,传入节点位置获取节点值
    def get_index(self,index):
        if index < 0:
            raise IndexError("index out of range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of range")
            p = p.next
        return p.val