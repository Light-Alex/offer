'''
题目: 旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
# 方法二：遍历，时间复杂度：O(n)

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        minNum = rotateArray[0]

        for i in rotateArray:
            minNum = i if i < minNum else minNum

        return minNum

if __name__ == "__main__":
    s = Solution()
    array = [3,4,5,1,2]
    print(s.minNumberInRotateArray(array))