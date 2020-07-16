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

# 方法二: 动态规划

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
            # 存储的是长度为该索引下的最大乘积, 
            # 如果是0-3的话, 就不用再减值(辅助数组)
            prod = [0, 1, 2, 3]
            for i in range(4, number+1):
                maxNum = 0
                for j in range(1, number//2+1):
                    if prod[j] * prod[i-j] > maxNum:
                        maxNum = prod[j] * prod[i-j]
                prod.append(maxNum)

        return prod[number]