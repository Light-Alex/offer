'''
题目: 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
# 方法一：创建一个空的列表，先放奇数，后放偶数
# 时间复杂度：O(n)，空间复杂度：O(n)

class Solution:
    def reOrderArray(self, array):
        # write code here
        s = []
        for i in array:
            if i % 2 == 1:
                s.append(i)
        
        for i in array:
            if i % 2 == 0:
                s.append(i)
        
        return s

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6]
    s = Solution()
    print(s.reOrderArray(array))