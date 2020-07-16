'''
题目: 二叉树中和为某一值的路径

输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
             8
          /     \
         5       9
       /   \    /
      4     8  2
              /
             2
输入: 21
输出: [[8, 9, 2, 2], [8, 5, 8]]
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

# 使用广度优先
# 一个列表存结点，一个列表存路径，一个列表存结果

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        
        result = []
        nodeList = [root]
        pathList = [[root.val]]

        while nodeList:
            currentNode = nodeList[0]
            currentPath = pathList[0]

            # 若遍历到叶结点，判断当前路径的和是否与输入值相等，相等则放入result中（路径短的先遍历完，故先放入result中）
            if currentNode.left == None and currentNode.right == None:
                if sum(currentPath) == expectNumber:
                    result.insert(0, currentPath)
            
            if currentNode.left:
                tempNode = currentNode.left
                nodeList.append(tempNode)
                tempPath = copy.copy(currentPath)
                tempPath.append(tempNode.val)
                pathList.append(tempPath)
            
            if currentNode.right:
                tempNode = currentNode.right
                nodeList.append(tempNode)
                tempPath = copy.copy(currentPath)
                tempPath.append(tempNode.val)
                pathList.append(tempPath)
            
            nodeList.pop(0)
            pathList.pop(0)

        return result