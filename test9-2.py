'''
题目: 包含min函数的栈

定义栈的数据结构，请在该类型中实现一个
能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''
# 采用空间换时间的方式
# 方法二：另外创建一个栈，栈顶永远存最小的值
# 若原栈的栈顶比该栈的栈顶大则不存，该栈长度<=原栈长度

class Solution:
    
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minStack:
            if node < self.minStack[-1]:
                self.minStack.append(node)
        else:
            self.minStack.append(node)

    def pop(self):
        # write code here
        if self.stack == [] or self.minStack == []:
            return None
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        return self.stack.pop()

    def top(self):
        # write code here
        if self.stack == [] or self.minStack == []:
            return None
        return self.stack[-1]

    def min(self):
        # write code here
        if self.minStack == []:
            return None
        return self.minStack[-1]

if __name__ == "__main__":
    s = Solution()
    s.push(-1)
    s.push(3)
    s.push(0)
    s.push(8)
    s.pop()
    print(s.stack)
    print(s.minStack)