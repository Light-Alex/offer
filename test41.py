'''
题目: 矩形覆盖

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

# 方法：(求斐波那契数列第n个数)
# 大矩形的高度为2，宽度为n
# 设总共有f(n)种放法
# 当第一个小矩形竖着放时，有f(n-1)种放法
# 当第一个小矩形横着放时，有f(n-2)种放法
# 所以总共有f(n) = f(n-1) + f(n-2)种放法
# f(0) = 0, f(1) = 1, f(2) = 2, f(3) = 1 + 2 = 3, ....

class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        
        a = 1
        b = 2

        for i in range(3, number + 1):
            a, b = b, a+b
        
        return b

if __name__ == "__main__":
    number = 4
    s = Solution()
    print(s.rectCover(number))