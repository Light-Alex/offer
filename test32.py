'''
题目: 最小的K个数

输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
'''

# 使用大小为k的最大堆来进行处理，这里需要注意不是完全二叉树的情况
# 最大堆中保存的k个数为最小的k的数字

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        
        if k < 1 or len(tinput) < k:
            return []
        
        maxHeap = []
        maxHeapLen = len(tinput)
        
        for i in range(maxHeapLen):
            if i < k:
                self.createMaxHeap(tinput[i], maxHeap)
            else:
                self.adjustMaxHeap(tinput[i], maxHeap)
        maxHeap.sort()
        
        return maxHeap
        
        
    # 创建(插入)最大堆
    def createMaxHeap(self, num, maxHeap):
        maxHeap.append(num)
        currentIndex = len(maxHeap)-1
        while currentIndex != 0:
            parentIndex = (currentIndex - 1) >> 1
            if maxHeap[parentIndex] < maxHeap[currentIndex]:
                maxHeap[parentIndex], maxHeap[currentIndex] = maxHeap[currentIndex], maxHeap[parentIndex]
                currentIndex = parentIndex
            else:
                break

    # 调整最大堆(最大堆大小有限，有新值来需要做调整)
    def adjustMaxHeap(self, num, maxHeap):
        maxHeapLen = len(maxHeap)
        currentIndex = 0

        if num < maxHeap[currentIndex]:
            maxHeap[currentIndex] = num

            # 当前结点的下标需要小于堆列表的长度
            while currentIndex < maxHeapLen:
                # 左结点的下标
                leftIndex = currentIndex * 2 + 1
                # 右结点的下标
                rightIndex = currentIndex * 2 + 2
                # 找出左右结点值最大的那个结点的下标
                # 左右结点都在
                if rightIndex < maxHeapLen:
                    largerIndex = leftIndex if maxHeap[leftIndex] > maxHeap[rightIndex] else rightIndex
                # 只有左结点
                elif leftIndex < maxHeapLen:
                    largerIndex = leftIndex
                # 左右结点都没有
                else:
                    break

                # 若当前结点的值比值最大的子结点小，则进行交换
                if maxHeap[currentIndex] < maxHeap[largerIndex]:
                    maxHeap[currentIndex], maxHeap[largerIndex] = maxHeap[largerIndex], maxHeap[currentIndex]
                    currentIndex = largerIndex
                else:
                    break