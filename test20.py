'''
题目: 不用加减乘除做加法

写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

# 由于题目要求不能使用四则运算，那么就需要考虑使用位运算
# 两个数相加可以看成两个数的每个位先相加，但不进位，然后在加上进位的数值
# 使用异或和与操作(^, &)

class Solution:
    def Add(self, num1, num2):
        # write code here

        while num2:

            xorNum = (num1 ^ num2) & 0xFFFFFFFF
            andNum = ((num1 & num2) << 1) & 0xFFFFFFFF

            num1 = xorNum
            num2 = andNum
        
        # return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)

        # 相加的和为正数
        if num1 <= 0x7FFFFFFF:
            return num1
        
        # 相加的和为负数
        else:
            return ~(num1 ^ 0xFFFFFFFF)
        

if __name__ == "__main__":
    a = -1
    b = -5
    print(a&0xFFFFFFFF)
    print(b&0xFFFFFFFF)
    # print(0xFFFFFFFF)
    s = Solution()
    print(s.Add(a, b))
    # print(0b11111111111111111111111111111010)
    # print(0b11111111111111111111111111111010 ^ 0xFFFFFFFF)
    print(~5)
    print(~-5)