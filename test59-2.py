'''
题目: 构建乘积数组

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''

# 方法二: 
# A = [2, 3, 4, 5, 6]
# 设B[0] = 1, B后面的数依次保存A前面乘积的结果(乘到倒数第二个)
# B = [1, 2, 6, 24, 120]
# 120 = 2 * 3 * 4 * 5, 不差值
# 24 = 2 * 3 * 4,      差 6
# 6 = 2 * 3,           差 5 * 6
# 2 = 1 * 2,           差 4 * 5 * 6
# 1 = 1,               差 3 * 4 * 5 * 6

class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        if length <= 1:
            return []
        
        B = [1]

        for i in range(length-1):
            B.append(B[i]*A[i])
        
        temp = 1

        for i in range(length-2, -1, -1):
            temp = temp * A[i+1]
            B[i] = B[i] * temp
        
        return B

if __name__ == "__main__":
    A = [2, 3, 4, 5, 6]
    s = Solution()
    print(s.multiply(A))