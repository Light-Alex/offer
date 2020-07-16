'''
题目: 第一个只出现一次的字符

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.
'''

# 方法一：
# 使用有序字典对字符串中的每一个字符进行计数
# 返回总数为1的第一个字符的位置
# 没有则返回-1

import collections

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        
        result = collections.OrderedDict()

        for i in s:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        
        tempChar = None

        for i in result:
            if result[i] == 1:
                tempChar = i
                break
        
        return s.index(tempChar) if tempChar else -1

if __name__ == "__main__":
    a = 'google'
    s = Solution()
    print(s.FirstNotRepeatingChar(a))