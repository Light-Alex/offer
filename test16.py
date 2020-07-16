'''
题目: 两个链表的第一个公共结点

输入两个链表，找出它们的第一个公共结点。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 两个链表长度相等时
# 两个指针同时往前走，直到走到相同结点

# 两个链表长度不等时
# 寻找两个链表长度的差值为k
# 让长的链表先走k步，使得两个链表的指针从相同长度的起点出发
# 两个指针同时往前走，直到走到相同结点

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pTmp1 = pHead1
        pTmp2 = pHead2

        # 两个链表长度相等时
        # 两个指针同时往前走，直到走到相同结点
        while pTmp1 and pTmp2:
            if pTmp1 == pTmp2:
                return pTmp1
            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next

        if pTmp1:
            k = 0
            while pTmp1:
                pTmp1 = pTmp1.next
                k += 1

            pTmp1 = pHead1
            for i in range(k):
                pTmp1 = pTmp1.next
            pTmp2 = pHead2

            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            
            return pTmp1
        
        else:
            k = 0
            while pTmp2:
                pTmp2 = pTmp2.next
                k += 1

            pTmp2 = pHead2
            for i in range(k):
                pTmp2 = pTmp2.next
            pTmp1 = pHead1

            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            
            return pTmp2

