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

'''
例如:
输入: [1,2,3,4,5,6,7,0]
逆序对: (1, 0) (2, 0) (3, 0) (4, 0) (5, 0) (6, 0) (7, 0)
'''
# 方法一: 时间复杂度 O(n^2)
# 对data进行排序:
# data: [1,2,3,4,5,6,7,0]
# dataSorted: [0,1,2,3,4,5,6,7]
# dataSorted的第一个元素为0, 它在data中的下标为7, 能构成7个逆序对
# 除去data中的0
# 按照上面操作依次遍历dataSorted中的元素, 找寻在data中的索引,即为逆序对的数量
# 累加，最终结果为逆序对总数

import copy

class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) <= 1:
            return 0
        
        dataSorted = copy.copy(data)
        dataSorted.sort()
        total = 0

        for i in dataSorted:
            total += data.index(i)
            data.remove(i)
        
        return total % 1000000007

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,0]
    s = Solution()
    print(s.InversePairs(data))