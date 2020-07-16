'''
题目: 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）：
它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
             8
          /     \
         5       9
       /   \    /
      4     6  7 

后续序列：[4, 6, 5, 7, 9, 8]
'''

# 方法：
# 后序遍历的序列中，最后一个数字是树的根节点 ，数组中前面的数字可以分为两部分：
# 第一部分是左子树节点的值，都比根节点的值小；
# 第二部分是右子树节点的值，都比根节点的值大，后面用递归分别判断前后两部分是否符合以上原则

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == None or sequence == []:
            return False
        
        length = len(sequence)
        rootNum = sequence[length-1]

        # 在二叉搜索树中左子树节点小于根节点
        for i in range(length):
            if sequence[i] > rootNum:
                break
        # 二叉搜索树中右子树的节点都大于根节点
        for j in range(i, length):
            if sequence[j] < rootNum:
                return False
        
        # 判断左子树是否为二叉搜索树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        
        # 判断右子树是否为二叉搜索树
        right = True
        if i < length-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        
        return left and right
