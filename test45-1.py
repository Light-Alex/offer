'''
题目: 把数组排成最小的数

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# 方法一：递归

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here

        def FindMinNumber(numbers):

            if len(numbers) <= 1:
                return numbers
            
            res = set()

            for i in range(len(numbers)):
                for j in FindMinNumber(numbers[:i] + numbers[i+1:]):
                    res.add(str(numbers[i])+str(j))
                
            return sorted(res)
        
        return int(FindMinNumber(numbers)[0]) if FindMinNumber(numbers) != [] else ''

if __name__ == "__main__":
    # numbers = [3, 32, 321]
    numbers = []
    s = Solution()
    print(s.PrintMinNumber(numbers))