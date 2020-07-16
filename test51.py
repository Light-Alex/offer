'''
题目: 和为S的连续正数序列

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述::
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''

# 方法: 使用两个指针
# 小指针plow初始化为1
# 大指针phigh初始化为2
# 每次计算小指针和大指针间的总和total
# 若total < tsum, 则phigh+=1
# 若total > tsum, 则plow+=1
# 若total = tsum, 则保存当前结果, plow+=1(phigh+=1)

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        pslow = 1
        phigh = 2
        result = []

        while pslow < phigh:
            total = (pslow + phigh) * (phigh - pslow + 1) / 2
            tempList = []
            if total < tsum:
                phigh += 1
            elif total == tsum:
                for i in range(pslow, phigh+1):
                    tempList.append(i)
                result.append(tempList)
                pslow += 1
            else:
                pslow += 1
        
        return result
    
if __name__ == "__main__":
    tsum = 100
    s = Solution()
    print(s.FindContinuousSequence(tsum))