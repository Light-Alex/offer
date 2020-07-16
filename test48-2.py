'''
题目: 数字在排序数组中出现的次数

统计一个数字在排序数组中出现的次数。
'''

# 方法二: 因为为排序数组，所以可以使用折半查找(非递归版)

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        length = len(data)

        if length == 0:
            return 0
        
        left = 0
        right = length - 1
        
        count = 0

        while left <= right:
            mid = (left + right) // 2
            if k > data[mid]:
                left = mid + 1
            elif k == data[mid]:
                count += 1
                data.pop(mid)
                right = right - 1
            else:
                right = mid - 1
        
        return count

if __name__ == "__main__":
    a = [1, 2, 2, 4, 5, 6]
    s = Solution()
    print(s.GetNumberOfK(a, 5))
    