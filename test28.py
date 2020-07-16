'''
题目: 从上往下打印二叉树

从上往下打印出二叉树的每个节点，同层节点从左至右打印。
             8                      
    	   /   \                   
    	  6     10               
    	 / \   /  \             
    	5   7 9   11      
[8, 6, 10, 5, 7, 9, 11]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        
        nodeList = [root]
        result = [root.val]

        while nodeList:
            tempNode = nodeList[0]

            if tempNode.left:
                leftNode = tempNode.left
                nodeList.append(leftNode)
                result.append(leftNode.val)
        
            if tempNode.right:
                rightNode = tempNode.right
                nodeList.append(rightNode)
                result.append(rightNode.val)

            # 每次删除nodeList的第一个元素
            nodeList.pop(0)

        return result
