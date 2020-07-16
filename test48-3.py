'''
题目: 数字在排序数组中出现的次数

统计一个数字在排序数组中出现的次数。
'''

# 方法三: 因为为排序数组，所以可以使用折半查找(递归版)

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        length = len(data)

        if length == 0:
            return 0
        
        global count
        count = 0

        def BinarySearch(data, k):
            global count
            
            length = len(data)

            if length == 0:
                return None

            if length == 1:
                if data[0] == k:
                    count += 1
                return None
            
            left = 0
            right = length - 1
            mid = (left + right) // 2

            if k < data[mid]:
                BinarySearch(data[:mid], k)
            elif k == data[mid]:
                count += 1
                BinarySearch(data[:mid]+data[mid+1:], k)
            else:
                BinarySearch(data[mid+1:], k)

        BinarySearch(data, k)    

        return count

if __name__ == "__main__":
    a = [1,2,3,3,3,3,4,5]
    s = Solution()
    print(s.GetNumberOfK(a, 3))
    