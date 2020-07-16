'''
题目: 数据流中的中位数

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值(小数)。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''

# 方法一：无封装版本
# 使用一个最大堆（放较小的数,左）和一个最小堆（放较大的数，右）来进行处理
# 最大堆和最小堆依次增加数据
# 再往最大堆添加数据时，若该数字比最小堆的根元素大，则先与最小堆根元素交换，调整最小堆，再将该数字(交换前最小堆的根元素)添加到最大堆，否则直接插入最大堆
# 再往最小堆添加数据时，若该数字比最大堆的根元素小，则先与最大堆根元素交换，调整最大堆，再将该数字(交换前最大堆的根元素)添加到最小堆，否则直接插入最小堆
# 最终
# 若最大堆和最小堆大小相等，则中位数为最大堆根元素和最小堆根元素的平均数
# 若最大堆大小比最小堆大，则中位数为最大堆根元素

class Solution:
    def __init__(self):
        self.smallerNumberMaxHeap = []
        self.largerNumberMinHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0

    def Insert(self, num):
        # write code here
        # 往大顶堆插数据
        if self.maxHeapCount == self.minHeapCount:
            self.maxHeapCount += 1
            # 只在第一次插大顶堆时做判断（第一次插小顶堆时不做判断）
            if len(self.smallerNumberMaxHeap) == 0:
                self.createMaxHeap(num)
            else:
                # 再往最大堆添加数据时，若该数字比最小堆的根元素大，则先与最小堆根元素交换
                # 调整最小堆，再将该数字(交换前最小堆的根元素)添加到最大堆，否则直接插入最大堆
                if num > self.largerNumberMinHeap[0]:
                    # num, self.largerNumberMinHeap[0] = self.largerNumberMinHeap[0], num
                    tempNum = self.largerNumberMinHeap[0]
                    self.adjustMinHeap(num)
                    self.createMaxHeap(tempNum)
                else:
                    self.createMaxHeap(num)
        # 往小顶堆插数据
        else:
            self.minHeapCount += 1
            # 再往最小堆添加数据时，若该数字比最大堆的根元素小，则先与最大堆根元素交换
            # 调整最大堆，再将该数字(交换前最大堆的根元素)添加到最小堆，否则直接插入最小堆
            if num < self.smallerNumberMaxHeap[0]:
                # num, self.smallerNumberMaxHeap[0] = self.smallerNumberMaxHeap[0], num
                tempNum = self.smallerNumberMaxHeap[0]
                self.adjustMaxHeap(num)
                self.createMinHeap(tempNum)
            else:
                self.createMinHeap(num)
        
        # print(self.smallerNumberMaxHeap)
        # print(self.largerNumberMinHeap)
            

    def GetMedian(self):
        # write code here
        return self.smallerNumberMaxHeap[0] if self.maxHeapCount > self.minHeapCount else float(self.smallerNumberMaxHeap[0] + self.largerNumberMinHeap[0]) / 2

    
    # 创建(插入)最大堆
    def createMaxHeap(self, num):
        self.smallerNumberMaxHeap.append(num)
        currentIndex = len(self.smallerNumberMaxHeap)-1
        while currentIndex != 0:
            # 父结点的下标
            parentIndex = (currentIndex - 1) >> 1
            if self.smallerNumberMaxHeap[parentIndex] < self.smallerNumberMaxHeap[currentIndex]:
                self.smallerNumberMaxHeap[parentIndex], self.smallerNumberMaxHeap[currentIndex] = self.smallerNumberMaxHeap[currentIndex], self.smallerNumberMaxHeap[parentIndex]
                currentIndex = parentIndex
            else:
                break

    # 调整最大堆(最大堆大小固定，有新值来需要做调整)
    def adjustMaxHeap(self, num):
        maxHeapLen = len(self.smallerNumberMaxHeap)
        currentIndex = 0

        if num < self.smallerNumberMaxHeap[currentIndex]:
            self.smallerNumberMaxHeap[currentIndex] = num

            # 当前结点的下标需要小于堆列表的长度
            while currentIndex < maxHeapLen:
                # 左结点的下标
                leftIndex = currentIndex * 2 + 1
                # 右结点的下标
                rightIndex = currentIndex * 2 + 2
                # 找出左右结点值最大的那个结点的下标
                # 左右结点都在
                if rightIndex < maxHeapLen:
                    largerIndex = leftIndex if self.smallerNumberMaxHeap[leftIndex] > self.smallerNumberMaxHeap[rightIndex] else rightIndex
                # 只有左结点
                elif leftIndex < maxHeapLen:
                    largerIndex = leftIndex
                # 左右结点都没有
                else:
                    break

                # 若当前结点的值比值最大的子结点小，则进行交换
                if self.smallerNumberMaxHeap[currentIndex] < self.smallerNumberMaxHeap[largerIndex]:
                    self.smallerNumberMaxHeap[currentIndex], self.smallerNumberMaxHeap[largerIndex] = self.smallerNumberMaxHeap[largerIndex], self.smallerNumberMaxHeap[currentIndex]
                    currentIndex = largerIndex
                else:
                    break

    # 创建(插入)最小堆
    def createMinHeap(self, num):
        self.largerNumberMinHeap.append(num)
        minHeapLen = len(self.largerNumberMinHeap)
        currentIndex = minHeapLen - 1
        while currentIndex != 0:
            # 父结点的下标
            parentIndex = (currentIndex - 1) >> 1
            if self.largerNumberMinHeap[currentIndex] < self.largerNumberMinHeap[parentIndex]:
                self.largerNumberMinHeap[currentIndex], self.largerNumberMinHeap[parentIndex] = self.largerNumberMinHeap[parentIndex], self.largerNumberMinHeap[currentIndex]
                currentIndex = parentIndex
            else:
                break

    # 调整最小堆(最小堆大小固定，有新值来需要做调整)
    def adjustMinHeap(self, num):
        minHeapLen = len(self.largerNumberMinHeap)
        # 当前结点的下标
        currentIndex = 0

        if num > self.largerNumberMinHeap[currentIndex]:
            self.largerNumberMinHeap[currentIndex] = num

            while currentIndex < minHeapLen:
                # 左结点的下标
                leftIndex = currentIndex * 2 + 1
                # 右结点的下标
                rightIndex = currentIndex * 2 + 2

                # 找出子结点中值较小的结点的下标
                # 存在左右结点(leftIndex < rightIndex)
                if rightIndex < minHeapLen:
                    smallerIndex = leftIndex if self.largerNumberMinHeap[leftIndex] < self.largerNumberMinHeap[rightIndex] else rightIndex
                # 只存在左结点
                elif leftIndex < minHeapLen:
                    smallerIndex = leftIndex
                # 无子结点
                else:
                    break

                # 当前结点的值若比子结点中较小值大则进行交换，否则退出循环
                if self.largerNumberMinHeap[currentIndex] > self.largerNumberMinHeap[smallerIndex]:
                    self.largerNumberMinHeap[currentIndex], self.largerNumberMinHeap[smallerIndex] = self.largerNumberMinHeap[smallerIndex], self.largerNumberMinHeap[currentIndex]
                    currentIndex = smallerIndex
                else:
                    break

if __name__ == "__main__":
    s = Solution()
    for i in [5,2,3,4,1,6,7,0,8]:
        s.Insert(i)
        print(s.GetMedian())