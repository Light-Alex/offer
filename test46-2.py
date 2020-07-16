'''
题目: 第一个只出现一次的字符

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.
'''

# 方法二:
# 使用str.count()方法

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        
        return -1

if __name__ == "__main__":
    a = 'google'
    s = Solution()
    print(s.FirstNotRepeatingChar(a))