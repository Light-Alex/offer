'''
题目: 删除链表中重复的结点

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法: 创建一个头结点, 以处理第一个结点是重复结点的情况
# 1、创建两个指针pre, last
# 2、pre指针指向重复结点前一个指针
# 3、last指针指向pre指针后一个结点, 用于判断重复结点

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return None
        
        headNode = ListNode(0)
        headNode.next = pHead

        pre = headNode
        last = headNode.next

        while last and last.next:
            if last.val == last.next.val:
                while last.next and last.val == last.next.val:
                    last = last.next
                pre.next = last.next
            else:
                pre = pre.next
            
            last = pre.next

        return headNode.next

if __name__ == "__main__":
    while None and None.next:
        print(1)