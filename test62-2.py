'''
题目: 字符流中第一个不重复的字符

请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
'''

# 方法二: 
# 使用两个列表
# 第一个列表保存所有出现过的字符(只保存一次)
# 第二个列表保存出现过一次的字符: 到达的字符在第一个列表没出现过, 则添加到该列表中, 到达的字符在第一个列表出现过, 则从该列表中取出该字符(若该字符存在的话)

class Solution:
    # 返回对应char
    def __init__(self):
        # 按顺序保存所有出现过的字符(只保存一次)
        self.allCharOnce = []
        # 按顺序保存所有只出现一次的字符
        self.firstChar = []

    def FirstAppearingOnce(self):
        # write code here
        return self.firstChar[0] if self.firstChar else '#'
        
    def Insert(self, char):
        # write code here
        if char not in self.allCharOnce:
            self.allCharOnce.append(char)
            self.firstChar.append(char)
        elif char in self.firstChar:
            self.firstChar.pop(self.firstChar.index(char))
        

if __name__ == "__main__":
    a = 'helloworld'
    s = Solution()
    for i in a:
        print(s.FirstAppearingOnce())
        s.Insert(i)
    
    print(s.FirstAppearingOnce())