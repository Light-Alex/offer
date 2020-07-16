'''
题目: 斐波那契数列

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''
# 保留前两次结果，时间复杂度为n

class Solution:
    def Fibonacci(self, n):
        # write code here
        # n = 0 f(0) = 0
        if n == 0:
            return 0
        # n = 1 f(1) = 1
        if n == 1:
            return 1

        
        a = 0
        b = 1
        ret = 0
        for i in range(n-1):
            ret = a + b
            a = b
            b = ret
        return ret
        
if __name__ == "__main__":
    s = Solution()
    print(s.Fibonacci(4))