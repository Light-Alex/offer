'''
题目: 二叉搜索树的第k个结点

给定一棵二叉搜索树（二叉排序树），请找出其中的第k小的结点。
例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
二叉搜索树：
            5
          /   \
         3     7
        / \   / \
       2   4 6   8

中序序列: [2, 3, 4, 5, 6, 7, 8]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法：二叉搜索树的中序序列是由小到大排好序的序列，所以第k小的数字是该序列第k个数字

# 中序遍历非递归版

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here

        if pRoot == None:
            return None
        
        result = []
        stack = []
        currentNode = pRoot

        while stack or currentNode:
            if currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                node = stack.pop()
                result.append(node)
                currentNode = node.right
        
        if k < 1 or k > len(result):
            return None
        
        return result[k-1]

if __name__ == "__main__":
    t1 = TreeNode(5)
    t2 = TreeNode(3)
    t3 = TreeNode(7)
    t4 = TreeNode(2)
    t5 = TreeNode(4)
    t6 = TreeNode(6)
    t7 = TreeNode(8)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7

    s = Solution()
    print(s.KthNode(t1, 3).val)