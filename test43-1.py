'''
题目: 顺时针打印矩阵

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

# 方法一：
# 可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
# 例如 
# 1 2 3
# 4 5 6
# 7 8 9
# 输出并删除第一行后，再进行一次逆时针旋转，就变成：
# 6 9
# 5 8
# 4 7
# 继续重复上述操作即可。

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                matrix = self.contrarotate(matrix)
        return result
    
    # 逆时针旋转矩阵
    def contrarotate(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        newMarix = []

        for i in range(column-1, -1, -1):
            tempList = []
            for j in range(row):
                tempList.append(matrix[j][i])
                # print(j, i)
            newMarix.append(tempList)
        
        return newMarix

if __name__ == "__main__":
    array = [[1],[2],[3],[4],[5]]
    s = Solution()
    # print(s.contrarotate(array))
    print(s.printMatrix(array))