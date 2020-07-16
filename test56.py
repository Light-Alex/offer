'''
题目: 求1+2+3+...+n

求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

# 方法: 利用短路求值的原理, 递归到self.Sum_Solution(0)终止, 因为0 < 1, self.Sum_Solution(0) = False, False + 1 = 1
# Python中, True和False用于计算时, True = 1, False = 0, 例如True + 0 = 1, False + 0 = 0

class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n >= 1 and self.Sum_Solution(n-1) + n

if __name__ == "__main__":
    a = 5
    s = Solution()
    print(s.Sum_Solution(a))