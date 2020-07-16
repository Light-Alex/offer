'''
题目: 丑数

把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

# 定义三个指针，这三个指针分别乘以2、3和5
# 每次乘以对应数后，值最小的指针往前挪一步

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here

        if index < 1:
            return 0

        uglyList = [1]
        twoPointer = 0
        threePointer = 0
        fivePointer = 0

        for i in range(index-1):
            uglyList.append(min(2*uglyList[twoPointer], 3*uglyList[threePointer], 5*uglyList[fivePointer]))
            if uglyList[-1] == 2*uglyList[twoPointer]:
                twoPointer += 1
            if uglyList[-1] == 3*uglyList[threePointer]:
                threePointer += 1
            if uglyList[-1] == 5*uglyList[fivePointer]:
                fivePointer += 1
        
        return uglyList[-1]

if __name__ == "__main__":
    index = 10
    s = Solution()
    print(s.GetUglyNumber_Solution(index))