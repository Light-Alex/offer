'''
题目: 平衡二叉树

输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
                10
              /    \
             1      2
              \   /   \
               8 7     9
                  \
                   6
'''
# 平衡二叉树（Balanced Binary Tree）具有以下性质：
# 它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树
# 方法二: 自下而上, 加上剪枝, 时间复杂度: O(n)

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return True if self.TreeDepth(pRoot) != -1 else False
    
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        
        left = self.TreeDepth(pRoot.left)

        # 剪枝的思想
        if left == -1:
            return -1
        
        right = self.TreeDepth(pRoot.right)

        # 剪枝的思想
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1

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
    print(s.IsBalanced_Solution(t1))