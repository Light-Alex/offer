'''
题目: 跳台阶

一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
'''
# 类似斐波那契数列
# f(1) = 1
# f(2) = 2
# f(n) = f(n-1) + f(n-2)

class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 1:
            return 0

        if number == 1:
            return 1

        if number == 2:
            return 2
        
        a = 1
        b = 2
        ret = 0
        for i in range(3, number+1):
            ret = a + b
            a = b
            b = ret
        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.jumpFloor(4))