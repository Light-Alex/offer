'''
题目: 表示数值的字符串

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''

# 方法: 实现两个函数, 分别判断一个字符串是否是整数或小数
# 若字符串中存在'e'或'E', 则'e'或'E'前半部分应该是整数或小数, 'e'或'E'后半部分应该是整数
# 若字符串中不存在'e'或'E', 则判断该字符串是否是整数或小数

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if s == '' or s == '+' or s == '-' or s.count('e') + s.count('E') > 1:
            return False
        
        if 'e' in s:
            index = s.index('e')
            return self.isDecimal(s[:index]) and self.isInteger(s[index+1:])
        elif 'E' in s:
            index = s.index('E')
            return self.isDecimal(s[:index]) and self.isInteger(s[index+1:])
        else:
            return self.isDecimal(s)

    # 判断一个字符串是否是整数
    def isInteger(self, s):
        if s == '' or s == '+' or s == '-':
            return False
        
        # 是否有符号位
        sign = 0

        if s[0] == '+' or s[0] == '-':
            sign = 1
        
        for i in range(sign, len(s)):
            if s[i] < '0' or s[i] > '9':
                return False
        
        return True
    
    # 判断一个字符串是否是小数(整数)
    def isDecimal(self, s):
        if s == '' or s == '+' or s == '-' or s.count('.') > 1:
            return False
        
        # 是否有符号位
        sign = 0

        if s[0] == '+' or s[0] == '-':
            sign = 1
        
        # if s[sign] == '.':
        #     return False
        
        for i in range(sign, len(s)):
            if (s[i] < '0' or s[i] > '9') and s[i] != '.':
                return False

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isNumeric('5e2'))