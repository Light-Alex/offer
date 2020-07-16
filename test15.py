'''
题目: 复杂链表的复制

输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

# 复制一个一样的node，并且添加到之前链表的每一个node后面
# 实现新建node的random的指向
# 断开原来的node和新的node之间的连接

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        pTmp = pHead
        
        if pTmp == None:
            return None
        
        # 复制一个一样的node，并且添加到之前链表的每一个node后面
        while pTmp:
            node = RandomListNode(pTmp.label)
            node.next = pTmp.next
            pTmp.next = node
            pTmp = node.next
        
        # 实现新建node的random的指向
        pTmp = pHead
        newHead = pTmp.next
        while pTmp:
            if pTmp.random != None:
                pTmp.next.random = pTmp.random.next
            pTmp = pTmp.next.next
        
        # 断开原来的node和新的node之间的连接
        pTmp = pHead
        pTmp2 = newHead
        while pTmp:
            pTmp.next = pTmp2.next
            if pTmp2.next != None:
                pTmp2.next = pTmp2.next.next
            pTmp = pTmp.next
            pTmp2 = pTmp2.next
        
        return newHead
        
