'''
题目: 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# 方法一：使用字典
# dict[num] = count
# 时间复杂度：O(n)，空间复杂度：O(n)

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here

        numDict = {}
        length = len(numbers)

        for num in numbers:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
            
            if numDict[num] > length>>1:
                return num
        
        return 0

if __name__ == "__main__":
    numbers = [1,2,3,2,2,2,5,4,2]
    s = Solution()
    print(s.MoreThanHalfNum_Solution(numbers))