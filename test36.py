'''
题目: 按之字形顺序打印二叉树

请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
            t1
         /      \
       t2       t3
      /  \     /  \
    t4    t5  t6   t7 

result: [[1], [3, 2], [4, 5, 6, 7]]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用两个栈实现

class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        
        stack1 = [pRoot]
        stack2 = []
        result = []

        while stack1 or stack2:
            tempList1 = []
            tempList2 = []
            while stack1:
                currentNode = stack1.pop()
                tempList1.append(currentNode.val)
                if currentNode.left:
                    stack2.append(currentNode.left)
                if currentNode.right:
                    stack2.append(currentNode.right)
            
            if tempList1:
                result.append(tempList1)

            while stack2:
                currentNode = stack2.pop()
                tempList2.append(currentNode.val)
                if currentNode.right:
                    stack1.append(currentNode.right)
                if currentNode.left:
                    stack1.append(currentNode.left)
            
            if tempList2:
                result.append(tempList2)
        
        return result

if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7

    s = Solution()
    print(s.Print(t1))