'''
题目: 链表中倒数第k个结点

输入一个链表，输出该链表中倒数第k个结点。
'''
# 使用快慢指针，两指针间隔为k，当前面那个指针指向None时，
# 后面那个指针指向的结点为倒数第k个结点
# 同时若k>链表的长度，则返回None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        firstPoint = head
        secondPoint = head

        for i in range(k):
            if secondPoint == None:
                return None
            secondPoint = secondPoint.next

        while secondPoint:
            firstPoint = firstPoint.next
            secondPoint = secondPoint.next
        
        return firstPoint

if __name__ == "__main__":
    l = [3,2,1]
    for i in range(3):
        l[i] = ListNode(i+1)
    
    for i in range(2):
        l[i].next = l[i+1]
    
    p = l[0]

    s = Solution()
    print(s.FindKthToTail(p, 5))
        