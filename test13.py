'''
题目: 反转链表

输入一个链表，反转链表后，输出新链表的表头。
'''
# 使用3个指针，firstPoint, secondPoint, thirdPoint

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here

        if pHead == None:
            return None
        
        if pHead.next == None:
            return pHead

        firstPoint = pHead
        secondPoint = pHead.next
        thirdPoint = pHead.next.next

        firstPoint.next = None

        while thirdPoint != None:
            secondPoint.next = firstPoint
            firstPoint = secondPoint
            secondPoint = thirdPoint
            thirdPoint = thirdPoint.next
        
        secondPoint.next = firstPoint

        return secondPoint


if __name__ == "__main__":
    l = [3,2,1]
    for i in range(3):
        l[i] = ListNode(i+1)
    
    for i in range(2):
        l[i].next = l[i+1]
    
    p = l[0]

    s = Solution()
    print(s.ReverseList(p).val)


