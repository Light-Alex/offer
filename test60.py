'''
题目: 正则表达式匹配

请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        
        # 如果s和pattern都为空, 则返回True
        if len(s) == 0 and len(pattern) == 0:
            return True
        
        # 如果s不为空, pattern为空, 则返回False
        elif len(s) != 0 and len(pattern) == 0:
            return False
        
        # 如果s为空, pattern不为空, 则需要分情况讨论
        elif len(s) == 0 and len(pattern) != 0:
            # 如果pattern第一个字符为'*', 则返回False
            if pattern[0] == '*':
                return False
            
            # 如果pattern字符长度大于1, 同时pattern的第二个字符为'*', 则s不变, pattern后移两位递归判断, 相当于没有使用'*'
            elif len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            
            else:
                return False
        
        # s和pattern都不为空
        else:
            # 如果pattern的第二字符为'*'
            if len(pattern) > 1 and pattern[1] == '*':
                # 如果s的第一个字符和pattern的第一个字符不同, 同时pattern的第一个字符不为'.', 则s不变, pattern后移两位, 相当于没有使用'*'
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                else:
                    # 如果s[0]与pattern[0]相同或pattern[0]为'.'，且pattern[1]为*，这个时候有两种情况
                    # pattern后移2个，s不变；相当于把pattern前两位当成空，匹配后面的(不使用'*')
                    # pattern不变，s后移1个；相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位(使用'*'一次或多次)
                    return self.match(s, pattern[2:]) or self.match(s[1:],pattern)
            # pattern的第二字符不为'*'
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False

 
if __name__ == "__main__":
    s = 'aaa'
    pattern = 'a.a'
    # pattern = 'ab*ac*a'
    # pattern = 'aa.a'
    # pattern = 'ab*a'

    solution = Solution()
    print(solution.match(s, pattern))