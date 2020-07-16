'''
题目: 变态跳台阶

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
# f(1) = 1
# f(n) = f(n-1) + f(n-2) + ... + f(2) + f(1)
# f(n-1) = f(n-2) + f(n-3) + ... + f(2) + f(1)
# f(n) = 2f(n-1)

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number < 1:
            return 0
        
        if number == 1:
            return 1
        
        a = 1
        ret = 1
        for i in range(1, number):
            ret = 2*a
            a = ret
        
        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.jumpFloorII(3))