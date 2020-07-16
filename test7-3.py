'''
题目: 旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
# 方法三：折半查找，时间复杂度：O(logn)
# 最小的数即小于左边那个数
# if array[mid] < array[right] : right = mid - 1
# if array[mid] > array[right] : left = mid + 1

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        
        left = 0
        right = len(rotateArray)-1
        while left <= right:
            mid = (left + right) >> 1 # 整除2
            if rotateArray[mid] < rotateArray[mid-1]:
                return rotateArray[mid]
            
            elif rotateArray[mid] < rotateArray[right]:
                right = mid -1

            else:
                left = mid + 1 
        

if __name__ == "__main__":
    s = Solution()
    array = [3,4,5,1,2]
    print(s.minNumberInRotateArray(array))