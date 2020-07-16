'''
实现归并排序, 有效到达排序

                    [1,2,3,4,5,6,7,0]
                   /                 \
              [1,2,3,4]          [5,6,7,8]
              /        \          /      \
            [1,2]    [3,4]      [5,6]   [7,8]
            /   \    /   \      /   \   /   \
          [1]   [2][3]   [4]  [5]   [6][7]  [8]
'''

def MergeSort(tempList):
    length = len(tempList)
    if length <= 1:
        return tempList

    index = length // 2

    left = MergeSort(tempList[:index])
    right = MergeSort(tempList[index:])
    
    print(left)
    print(right)
    

    # 每次合并的列表
    result = []
    # 左边处理的数量
    l = 0
    # 右边处理的数量
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    print(result)
    print('-'*10)

    return result

if __name__ == "__main__":
    a = [9,8,7,5,6]
    print(MergeSort(a))