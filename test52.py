'''
题目: 和为S的两个数字

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S
如果有多对数字的和等于S，输出两个数的乘积最小的。

输出描述:
对应每个测试案例，输出两个数，小的先输出。
'''

# 输入: [1, 3, 5, 7, 9] 10
# 输出: [1, 9]
# 方法: 使用左右夹逼法
# 设一个left指向表头, 一个right指向表尾
# 若array[left] + array[right] < tsum, 则left += 1
# 若array[left] + array[right] > tsum, 则right -= 1
# 若array[left] + array[right] = tsum, 则返回[left, right](向中间靠拢, 两个数的乘积会变大)

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here

        left = 0
        right = len(array) - 1

        result = []

        while left < right:
            if array[left] + array[right] < tsum:
                left += 1
            elif array[left] + array[right] == tsum:
                result.append(array[left])
                result.append(array[right])
                break
            else:
                right -= 1

        return result

if __name__ == "__main__":
    array = [2, 3, 5, 7, 9, 10]
    tsum = 12
    s = Solution()
    print(s.FindNumbersWithSum(array, tsum))