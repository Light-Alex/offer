'''
题目: 二叉树的下一个结点

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
            2
          /   \
         1     3
        / \   / \
       5   6 0  -2
              \
               4

中序遍历：[5, 1, 6, 2, 0, 4, 3, -2]
'''

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# 方法：
# 1、有右子树的，那么下个结点就是右子树最左边的点
# 2、没有右子树的，也可以分成两类：
#   （1）是父节点左孩子，那么父节点就是下一个节点
#   （2）是父节点的右孩子，找他的父节点的父节点的父节点...直到当前结点是其父节点的左孩子位置。如果没有，那么他就是尾节点。

class Solution:
    def GetNext(self, pNode):
        # write code here
        # 有右子树的，那么下个结点就是右子树最左边的点
        if pNode.right:
            tempNode = pNode.right
            while tempNode.left:
                tempNode = tempNode.left
            return tempNode
        # 没有右子树的，也可以分成两类：
        #（1）是父节点左孩子，那么父节点就是下一个节点
        #（2）是父节点的右孩子，找他的父节点的父节点的父节点...直到当前结点是其父节点的左孩子位置。如果没有，那么他就是尾节点。
        else:
            tempNode = pNode
            while tempNode.next:
                if tempNode.next.left == tempNode:
                    return tempNode.next
                tempNode = tempNode.next
            # 没有找到
            return None