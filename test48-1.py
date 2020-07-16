'''
题目: 数字在排序数组中出现的次数

统计一个数字在排序数组中出现的次数。
'''

# 方法一: data.count(k)方法

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)

if __name__ == "__main__":
    a = [1, 2, 2, 4, 5]
    s = Solution()
    print(s.GetNumberOfK(a, 2))