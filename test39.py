'''
题目: 序列化二叉树

请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，
序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法：递归实现
'''
             10
           /    \
          5      6
         / \
        2   3
       /
      1

先序遍历:
序列化结果: ['10', '5', '2', '1', '#', '#', '#', '3', '#', '#', '6', '#', '#'] -> '10 5 2 1 # # # 3 # # 6 # #'
'''

class Solution:
    def Serialize(self, root):
        # write code here
        if root == None:
            return None
        
        result = []

        def preOrderRecursive(pRoot):
            if pRoot == None:
                result.append('#')
                return None

            result.append(str(pRoot.val))
            preOrderRecursive(pRoot.left)
            preOrderRecursive(pRoot.right)
        
        preOrderRecursive(root)
        return ' '.join(result)

    def Deserialize(self, s):
        # write code here
        if s == None:
            return None
        
        result = s.split()

        def dePreOrderRecursive():

            nodeVal = result.pop(0)

            if nodeVal == '#':
                return None
            
            node = TreeNode(int(nodeVal))

            leftNode = dePreOrderRecursive()
            rightNode = dePreOrderRecursive()

            node.left = leftNode
            node.right = rightNode

            return node
        
        return dePreOrderRecursive()



if __name__ == "__main__":
    t1 = TreeNode(10)
    t2 = TreeNode(5)
    t3 = TreeNode(6)
    t4 = TreeNode(2)
    t5 = TreeNode(3)
    t6 = TreeNode(1)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t4.left = t6

    s = Solution()
    print(s.Serialize(t1))