'''
题目: 用两个栈实现队列

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
class Solution:
    def __init__(self):
        self.acceptStack = []
        self.outputStack = []

    def push(self, node):
        # write code here
        self.acceptStack.append(node)

    def pop(self):
        # return xx
        if self.outputStack == []:
            while self.acceptStack != []:
                self.outputStack.append(self.acceptStack.pop())
            return self.outputStack.pop()
        else:
            return self.outputStack.pop()

if __name__ == "__main__":
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    s.push(4)
    print(s.pop())
