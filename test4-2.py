'''
题目: 二维数组中的查找

在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
# 1 2 3 4
# 2 5 6 7
# 3 6 8 10
# 4 7 9 11
# 方法二：与右上角元素比较，时间复杂度:O(n)
# 若target>4，则i+=1
# 若target<4，则j-=1

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = 0
        j = len(array[0]) - 1
        while i < len(array) and j >= 0:
            value = array[i][j]
            if target > value:
                i += 1
            elif target < value:
                j -= 1
            else:
                return True
        
        return False

if __name__ == "__main__":
    array = [[1,2,3,4],
            [2,5,6,7],
            [3,6,8,10],
            [4,7,9,11]]
    target = 8
    s = Solution()
    print(s.Find(target, array))