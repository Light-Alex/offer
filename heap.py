'''
最大堆和最小堆都是完全二叉树
完全二叉树：对于深度为K的，有n个结点的二叉树，当且仅当其每一个结点都与深度为K的满二叉树中编号从1至n的结点一一对应时称之为完全二叉树。（可以无右结点）
满二叉树：（国内）除最后一层无任何子节点外，每一层上的所有结点都有两个子结点的二叉树。
（国外）一棵满二叉树的每一个结点要么是叶子结点，要么它有两个子结点。

最大堆：最大堆（大顶堆，大根堆）要求根节点的关键字既大于或等于左子树的关键字值，又大于或等于右子树的关键字值。

               10
             /    \
            6      8
           / \
          5   3    

树的深度: 3
树的度: 2
树的高度: 3

用列表存储(广度优先)：[10, 6, 8, 5, 3] index:[0, 1, 2, 3, 4]
子结点找父结点: (index - 1) // 2
父结点找子结点: 
            左结点：index * 2 + 1
            右结点：index * 2 + 2


最小堆：最小堆是一种经过排序的完全二叉树，其中任一非终端节点的数据值均不大于其左子节点和右子节点的值。

               2
             /   \
            4     7
           / \
          6   8 
'''

# 创建(插入)最大堆
def createMaxHeap(num, maxHeap):
    maxHeap.append(num)
    currentIndex = len(maxHeap)-1
    while currentIndex != 0:
        # 父结点的下标
        parentIndex = (currentIndex - 1) >> 1
        if maxHeap[parentIndex] < maxHeap[currentIndex]:
            maxHeap[parentIndex], maxHeap[currentIndex] = maxHeap[currentIndex], maxHeap[parentIndex]
            currentIndex = parentIndex
        else:
            break

# 调整最大堆(最大堆大小固定，有新值来需要做调整)
def adjustMaxHeap(num, maxHeap):
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

# 创建(插入)最小堆
def createMinHeap(num, minHeap):
    minHeap.append(num)
    minHeapLen = len(minHeap)
    currentIndex = minHeapLen - 1
    while currentIndex != 0:
        # 父结点的下标
        parentIndex = (currentIndex - 1) >> 1
        if minHeap[currentIndex] < minHeap[parentIndex]:
            minHeap[currentIndex], minHeap[parentIndex] = minHeap[parentIndex], minHeap[currentIndex]
            currentIndex = parentIndex
        else:
            break

# 调整最小堆(最小堆大小固定，有新值来需要做调整)
def adjustMinHeap(num, minHeap):
    minHeapLen = len(minHeap)
    # 当前结点的下标
    currentIndex = 0

    if num > minHeap[currentIndex]:
        minHeap[currentIndex] = num

        while currentIndex < minHeapLen:
            # 左结点的下标
            leftIndex = currentIndex * 2 + 1
            # 右结点的下标
            rightIndex = currentIndex * 2 + 2

            # 找出子结点中值较小的结点的下标
            # 存在左右结点(leftIndex < rightIndex)
            if rightIndex < minHeapLen:
                smallerIndex = leftIndex if minHeap[leftIndex] < minHeap[rightIndex] else rightIndex
            # 只存在左结点
            elif leftIndex < minHeapLen:
                smallerIndex = leftIndex
            # 无子结点
            else:
                break
            
            # 当前结点的值若比子结点中较小值大则进行交换，否则退出循环
            if minHeap[currentIndex] > minHeap[smallerIndex]:
                minHeap[currentIndex], minHeap[smallerIndex] = minHeap[smallerIndex], minHeap[currentIndex]
                currentIndex = smallerIndex
            else:
                break

if __name__ == "__main__":
    maxHeap = []
    for i in range(5):
        createMaxHeap(i, maxHeap)
    print(maxHeap)
    adjustMaxHeap(-1, maxHeap)
    print(maxHeap)

    minHeap = []
    for i in [0, 2, 5, 1, -2, 3]:
        createMinHeap(i, minHeap)
    print(minHeap)
    adjustMinHeap(7, minHeap)
    print(minHeap)