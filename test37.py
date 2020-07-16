'''
题目: 把二叉树打印成多行

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
            t1
         /      \
       t2       t3
      /  \     /  \
    t4    t5  t6   t7 

result: [[1], [2, 3], [4, 5, 6, 7]]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用两个队列实现

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []

        queue1 = [pRoot]
        queue2 = []
        result = []

        while queue1 or queue2:
            tempList1 = []
            tempList2 = []

            while queue1:
                currentNode = queue1.pop(0)
                tempList1.append(currentNode.val)
                if currentNode.left:
                    queue2.append(currentNode.left)
                
                if currentNode.right:
                    queue2.append(currentNode.right)          
            if tempList1:
                result.append(tempList1)
            
            while queue2:
                currentNode = queue2.pop(0)
                tempList2.append(currentNode.val)
                if currentNode.left:
                    queue1.append(currentNode.left)
                
                if currentNode.right:
                    queue1.append(currentNode.right)
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