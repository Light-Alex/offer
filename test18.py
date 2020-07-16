'''
题目: 链表中环的入口结点

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 定义一个快慢指针判断是否有环
# 快指针一次走两步，慢指针一次走一步
# 若快指针走到空(或快指针的next为空)则没有环
# 若快慢指针相遇，则有环

# 有环的情况
# 若slow走了l的长度，则fast就走了2l的长度
# 若起点到入口结点的长度为s，slow在环里走的长度为d，slow在环内位置到入口结点的长度为m
# 则l = s + d
# 2l = s + (m + d) * n + d
# 由s + (m + d) * n + d = 2(s + d)推得, s = m + (n - 1) * (m + d)，(m + d)为环的长度
# 忽略(n - 1) * (m + d)部分(转圈相当于原地不动)，s = m
# 故两指针从起点和相遇位置同时出发，相遇处即为入口结点

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here

        if pHead == None:
            return None
        
        fastPointer = pHead
        slowPointer = pHead

        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                break
        
        if fastPointer == None or fastPointer.next == None:
            return None
        
        fastPointer = pHead

        while slowPointer != fastPointer:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        
        return slowPointer