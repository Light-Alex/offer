'''
题目: 构建乘积数组

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''

# 方法一: 利用Python列表切片实现

class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        if length <= 1:
            return []
        
        def MultiplyList(array):
            result = 1
            for i in array:
                result *= i
            
            return result
        
        B = []
        for i in range(length):
            B.append(MultiplyList(A[:i]+A[i+1:]))

        return B

if __name__ == "__main__":
    A = [1, 2, 3, 4]
    s = Solution()
    print(s.multiply(A))