'''
题目: 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
# 方法二：使用冒泡排序

class Solution:
    def reOrderArray(self, array):
        # write code here
        for i in range(len(array)-1):
            for j in range(len(array)-1-i):
                if array[j] % 2 == 0 and array[j+1] % 2 == 1:
                    array[j], array[j+1] = array[j+1], array[j]
        
        return array

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6]
    s = Solution()
    print(s.reOrderArray(array))