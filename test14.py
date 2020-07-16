'''
题目: 合并两个排序的链表

输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
'''
# 使用4个指针：
# 一个指针指向新的链表头
# 一个指针指向当前结点
# 一个指针指向pHead1链表中需要比较的那个结点
# 一个指针指向pHead2链表中需要比较的那个结点
# 1 2 3 6 8
# 4 7 10 12 13

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        
        if pHead2 == None:
            return pHead1
        
        newHead = pHead1 if pHead1.val < pHead2.val else pHead2

        currentPoint = newHead

        pTemp1 = pHead1
        pTemp2 = pHead2

        if newHead == pHead1:
            pTemp1 = pHead1.next
        else:
            pTemp2 = pHead2.next

        while pTemp1 and pTemp2:
            if pTemp1.val < pTemp2.val:
                currentPoint.next = pTemp1
                pTemp1 = pTemp1.next
            else:
                currentPoint.next = pTemp2
                pTemp2 = pTemp2.next

            currentPoint = currentPoint.next

        if pTemp1 == None:
            currentPoint.next = pTemp2
        else:
            currentPoint.next = pTemp1
        
        return newHead
