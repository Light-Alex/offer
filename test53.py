'''
题目: 左旋转字符串

汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
'''

# 方法: 找到变化前和变化后的对应关系
# 设变化前的下标为preIndex, 变化后的下标为latIndex, 字符串长度为length, 左移n
# 则latIndex = (length + preIndex - n % length) % length

import copy

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        
        length = len(s)
        if n < 0 or length == 0:
            return ''
        
        s = list(s)
        a = copy.copy(s)

        for i in range(length):
            index = (length + i - n % length) % length
            a[index] = s[i]

        return ''.join(a)

if __name__ == "__main__":
    s1 = 'abcXYZdef'
    s = Solution()
    print(s.LeftRotateString(s1, 3))
