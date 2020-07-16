'''
题目: 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# 方法二：遇到不同的数字就相互抵消掉，最后剩下的数字就可能是
# 出现次数超过数组长度一半的数字
# 时间复杂度：O(n)，空间复杂度：O(1)

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here

        current = 0
        currentCount = 0

        for num in numbers:
            if currentCount == 0:
                current = num
                currentCount = 1
            else:
                if num != current:
                    currentCount -= 1

                else:
                    currentCount += 1
        
        if currentCount == 0:
            return 0
        
        else:
            currentCount = 0

            for num in numbers:
                if num == current:
                    currentCount += 1
            
            if currentCount > len(numbers)>>1:
                return current
            else:
                return 0



if __name__ == "__main__":
    numbers = [1,2,3,2,2,2,5,4,2]
    s = Solution()
    print(s.MoreThanHalfNum_Solution(numbers))