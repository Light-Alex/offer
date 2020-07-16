'''
题目: 替换空格

请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
# 方法二：使用append()函数

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        a = []
        for i in s:
            if i == ' ':
                a.append('%20')
            else:
                a.append(i)
        
        return ''.join(a)

if __name__ == "__main__":
    s = Solution()
    source = 'We Are Happy'
    print(s.replaceSpace(source))