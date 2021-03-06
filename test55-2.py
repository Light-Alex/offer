'''
题目: 扑克牌顺子

LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了
他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。
现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。
为了方便起见,你可以认为大小王是0。
'''

# 方法二: 
# 1、如果输入的长度不为5, 返回False
# 2、如果存在相同的非零元素, 返回False
# 3、除了以上情况, 先对数组进行排序, 统计0的数量zeroNum, 从zeroNum开始(第一个非零元素)遍历数组, 若相邻元素差值 > 1
# 则zeroNum = zeroNum - 差值 - 1, 若遍历过程中zeroNum < 0, 则返回False, 否则返回True

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5:
            return False
        
        numbers.sort()
        zeroNum = numbers.count(0)
        for i in range(zeroNum, 4):
            if numbers[i+1] - numbers[i] > 1:
                zeroNum -= numbers[i+1] - numbers[i] - 1
                if zeroNum < 0:
                    return False
            elif numbers[i+1] - numbers[i] == 0:
                return False
            else:
                continue
        
        return True

if __name__ == "__main__":
    a = [0, 0, 1, 3, 5]
    s = Solution()
    print(s.IsContinuous(a))