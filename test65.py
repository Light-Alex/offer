'''
题目: 矩阵中的路径

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

# 方法: 
# 回溯法
# 遍历矩阵中的每一个位置

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False
        
        if not path:
            return True
        
        # 将字符串matrix转换成矩阵
        matrix = [list(matrix[i*cols:(i+1)*cols]) for i in range(rows)]
        
        # 遍历矩阵中的每一个位置
        for i in range(rows):
            for j in range(cols):
                # 找到该路径则返回True
                if self.search(matrix, i, j, path):
                    return True
        
        # 没有找到该路径则返回False
        return False
    
    def search(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            # 成功走到末尾返回True
            if not p[1:]:
                return True
            # 该位置走过了, 置为空
            matrix[i][j] = ''
            # 从该位置出发向周围四个方向走
            # 向上走一步, 能走通则返回True
            if i > 0 and self.search(matrix, i-1, j, p[1:]):
                return True
            # 向下走一步, 能走通则返回True
            if i < len(matrix) - 1 and self.search(matrix, i+1, j, p[1:]):
                return True
            # 向左走一步, 能走通则返回True
            if j > 0 and self.search(matrix, i, j-1, p[1:]):
                return True
            # 向右走一步, 能走通则返回True
            if j < len(matrix[0])-1 and self.search(matrix, i, j+1, p[1:]):
                return True
            
            # 若从该位置出发向周围四个方向都走不通, 则恢复该位置的值(其他路径可能会经过该位置), 并返回False
            matrix[i][j] = p[0]
            return False
        else:
            return False

if __name__ == "__main__":
    # matrix = ['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e']
    matrix = 'abcesfcsadee'
    # path = 'bcced'
    path = 'abcb'
    s = Solution()
    print(s.hasPath(matrix, 3, 4, path))