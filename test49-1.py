'''
题目: 二叉树的深度

输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
方法一: 先序遍历(非递归版)
                10
              /    \
             1      2
              \   /   \
               8 7     9
                  \
                   6
深度: 4
'''

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        depth = 0
        maxDepth = 0
        stack = []
        currentNode = pRoot

        while stack or currentNode:
            if currentNode:
                stack.append(currentNode)
                depth += 1
                currentNode = currentNode.left
            else:
                node = stack.pop()
                currentNode = node.right
                if not currentNode:
                    maxDepth = depth if depth > maxDepth else maxDepth
                    depth = len(stack)
        
        return maxDepth

if __name__ == "__main__":
    t1 = TreeNode(10)
    t2 = TreeNode(1)
    t3 = TreeNode(2)
    t4 = TreeNode(8)
    t5 = TreeNode(7)
    t6 = TreeNode(9)
    t7 = TreeNode(6)

    t1.left = t2
    t1.right = t3
    t2.right = t4
    t3.left = t5
    t3.right = t6
    t5.right = t7

    s = Solution()
    print(s.TreeDepth(t1))