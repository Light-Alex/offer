'''
题目: 剪绳子

给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）

输出描述:
输出答案。

示例:
输入: 8
输出: 18
'''

# 方法一: 贪心算法

class Solution:
    def cutRope(self, number):
        # write code here
        result = 0
        if number <= 1:
            return 0
        elif number == 2:
            return 1
        elif number == 3:
            return 2
        else:
            if number % 3 == 0:
                result = 3 ** (number // 3)
            elif number % 3 == 1:
                result = 3 ** (number // 3 - 1) * 4
            else:
                result = 3 ** (number // 3) * (number % 3)
        return result