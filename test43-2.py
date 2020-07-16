'''
题目: 顺时针打印矩阵

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

# 方法二：
# 使用pop(),pop(0)顺时针打印
# 1  2  3  4  5 
# 6  7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20
 
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            if matrix and matrix[0]:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        
        return result

        
if __name__ == "__main__":
    array = [[1],[2],[3],[4],[5]]
    s = Solution()
    # print(s.contrarotate(array))
    print(s.printMatrix(array))