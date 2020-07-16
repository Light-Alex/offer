'''
题目: 从尾到头打印链表

输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''
# 使用一个队列依次存放单链表的值

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ArrayList = []
        while listNode:
            ArrayList.insert(0, listNode.val)
            listNode = listNode.next
        return ArrayList

if __name__ == "__main__":
    l = [3,2,1]
    for i in range(3):
        l[i] = ListNode(i+1)
    
    for i in range(2):
        l[i].next = l[i+1]
    
    p = l[0]

    s = Solution()
    print(s.printListFromTailToHead(p))