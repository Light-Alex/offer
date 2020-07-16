'''
题目: 机器人的运动范围

地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

# 方法: 回溯法, 从[0][0]位置出发
# 创建元素全为0的行数为rows, 列数为cols的矩阵, 记录矩阵每个位置被访问的次数
# 每成功访问矩阵的一个位置, 该位置上的值+1
# 该位置能够被访问需要满足三个条件:
# 1、i, j在矩阵范围内, 没有越界
# 2、行坐标和列坐标的数位之和<=threshold
# 3、矩阵上该位置的值为0(没有被访问过)

class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows < 1 or cols < 1:
            return 0
        
        # 创建元素全为0的矩阵
        matrix = [[0 for j in range(cols)] for i in range(rows)]

        self.search(threshold, 0, 0, matrix)
        # print(matrix)
        return self.count
    
    def search(self, threshold, i, j, matrix):
        if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold and matrix[i][j]==0:
            
            # 经过该位置时, 该位置上的元素+1(使其不等于0, 以避免重复经过此处)
            matrix[i][j] += 1
            self.count += 1
            self.search(threshold, i-1, j, matrix)
            self.search(threshold, i+1, j, matrix)
            self.search(threshold, i, j-1, matrix)
            self.search(threshold, i, j+1, matrix)
        else:
            return 0

if __name__ == "__main__":
    threshold = 5
    rows = 10
    cols = 10
    s = Solution()
    print(s.movingCount(threshold, rows, cols))