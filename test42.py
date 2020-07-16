'''
题目: 数值的整数次方

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
'''

# 注意：需要考虑exponet > 0, exponent = 0和exponent < 0的情况

class Solution:
    def Power(self, base, exponent):
        # write code here

        if base == 0 and exponent == 0:
            return None
        
        if exponent == 0:
            return 1
        
        result = 1.0

        if exponent > 0:
            for i in range(exponent):
                result = result * base
        else:
            for i in range(-exponent):
                result = result * base
            result = 1 / result
        
        return result

if __name__ == "__main__":
    base = 2
    exponent = -3
    s = Solution()

    print(s.Power(base, exponent))