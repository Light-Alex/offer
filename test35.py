'''
题目: 对称的二叉树

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
                   8
                 /   \
                5     5
               / \   / \
              1   2 2   1
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 使用递归实现, 递归判断某结点的左结点和右结点的值是否相等

class Solution:

    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return self.isMirror(pRoot.left, pRoot.right)
    
    def isMirror(self, left, right):
        # 左右结点都为空，递归结束
        if left == None and right == None:
            return True
        # 左结点为空，右结点不为空，或左结点不为空，右结点为空，则不对称
        elif left == None or right == None:
            return False
        else:
            if left.val == right.val:
                return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
            else:
                return False