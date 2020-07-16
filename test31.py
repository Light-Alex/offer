'''
题目: 二叉搜索树与双向链表

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
             8
          /     \
         5       9
       /   \    /
      4     6  7 
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 使用非递归的中序遍历，中序序列元素两两间进行互指，进而将二叉搜索树转换为排序的双向链表

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        
        stack = []
        resultStack = []
        tempNode = pRootOfTree
        
        # 非递归的中序遍历
        while stack or tempNode:

            if tempNode:
                stack.append(tempNode)
                tempNode = tempNode.left
            else:
                node = stack.pop()
                resultStack.append(node)
                tempNode = node.right
        
        # 头结点
        result = resultStack[0]

        # 中序序列元素两两间进行互指
        while resultStack:
            node = resultStack.pop(0)
            if resultStack:
                node.right = resultStack[0]
                resultStack[0].left = node
        
        return result