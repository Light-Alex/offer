'''
题目: 二进制中1的个数

输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

# 正数的补码是其本身，负数的补码是其反码加1
# -2的补码：10000000000...0010 -> 11111111111...1101 + 1 -> 111111111111...1110
# 取后32位 n & 0xFFFFFFFF 
# 方法三：n & (n-1): 每次除去最后一个1


class Solution:
    def NumberOf1(self, n):
        # write code here

        n = 0xFFFFFFFF & n

        count = 0
        
        while n:
            n = n & (n-1)
            count += 1

        return count

if __name__ == "__main__":
    n = -8
    s = Solution()
    print(s.NumberOf1(n))