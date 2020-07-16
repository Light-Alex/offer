'''
题目: 把数组排成最小的数

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# 方法二：冒泡排序
# [a, b, c]
# 若 a+b < b+a，则a排在前面
# 例如2 21，因为221>212，所以21排在前面
# 两两比较，使用冒泡排序

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        length = len(numbers)

        if length == 0:
            return ''
        
        # 将整型列表转换成字符串列表
        numbers = list(map(str, numbers))
        
        for i in range(length - 1):
            for j in range(length - 1 - i):
                if numbers[j] + numbers[j+1] > numbers[j+1] + numbers[j]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        
        return ''.join(numbers)

if __name__ == "__main__":
    numbers = [3, 32, 321]
    # numbers = []
    s = Solution()
    print(s.PrintMinNumber(numbers))