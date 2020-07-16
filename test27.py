'''
题目: 二叉树的镜像

操作给定的二叉树，将其变换为源二叉树的镜像。

二叉树的镜像定义：源二叉树        镜像二叉树
             8                       8
    	   /   \                   /   \
    	  6     10               10     6 
    	 / \   /  \             /  \   / \
    	5   7 9   11           11   9 7   5
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用递归的方法，先处理根结点，再处理左结点，然后处理右节点

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        
        if root == None:
            return None
        
        root.left, root.right = root.right, root.left

        self.Mirror(root.left)
        self.Mirror(root.right)