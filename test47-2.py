'''
题目: 数组中的逆序对

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
注意: 题目保证输入的数组中没有的相同的数字
例如:
输入: [1,2,3,4,5,6,7,0]
逆序对: (1, 0) (2, 0) (3, 0) (4, 0) (5, 0) (6, 0) (7, 0)
输出: 7
'''

# 方法二：使用归并排序
'''
例如:
输入: [1,2,3,4,5,6,7,0]
逆序对: (1, 0) (2, 0) (3, 0) (4, 0) (5, 0) (6, 0) (7, 0)

                    [1,2,3,4,5,6,7,0]
                   /                 \
              [1,2,3,4]          [5,6,7,0]
              /        \          /      \
            [1,2]    [3,4]      [5,6]   [7,0]
            /   \    /   \      /   \   /   \
          [1]   [2][3]   [4]  [5]   [6][7]  [0]
'''

class Solution:
    def InversePairs(self, data):
        # write code here
        length = len(data)
        if length <= 1:
            return 0

        global total
        total = 0

        # 归并排序思想
        def MergeSort(dataList):
            global total
            length = len(dataList)

            if length <= 1:
                return dataList
            
            index = length // 2
            left = MergeSort(dataList[:index])
            right = MergeSort(dataList[index:])

            # 合并的列表(有小到大排序)
            result = []
            # 左边已处理的数字
            l = 0
            # 右边已处理的数字
            r = 0

            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    total += len(left) - l
                    r += 1
            
            result += left[l:]
            result += right[r:]

            return result
        
        MergeSort(data)
        return total % 1000000007

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,0]
    s = Solution()
    print(s.InversePairs(data))