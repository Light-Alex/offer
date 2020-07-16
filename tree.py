class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1. 深度优先
# 2. 广度优先

# 深度优先：
# 1. 先序遍历：根左右 (1, 2, 4, 5, 3, 6, 8, 7)
# 2. 中序遍历：左根右 (4, 2, 5, 1, 6, 8, 3, 7)
# 3. 后序遍历：左右根 (4, 5, 2, 8, 6, 7, 3, 1)

# 递归
# 先序遍历
def preOrderRecursive(root):
    if root == None:
        return None
    print(root.val)
    preOrderRecursive(root.left)
    preOrderRecursive(root.right)

# 中序遍历
def midOrderRecursive(root):
    if root == None:
        return None
    midOrderRecursive(root.left)
    print(root.val)
    midOrderRecursive(root.right)

# 后序遍历
def latOrderRecursive(root):
    if root == None:
        return None
    latOrderRecursive(root.left)
    latOrderRecursive(root.right)
    print(root.val)

# 非递归方式：使用栈
# 先序遍历
def preOrderStack(root):
    if root == None:
        return None
    stack = []
    tempNode = root
    while tempNode or stack:
        while tempNode:
            print(tempNode.val)
            stack.append(tempNode)
            tempNode = tempNode.left
    
        node = stack.pop()
        tempNode = node.right

# 中序遍历
def midOrderStack(root):
    if root == None:
        return None
    stack = []
    tempNode = root
    while tempNode or stack:
        while tempNode:
            stack.append(tempNode)
            tempNode = tempNode.left
    
        node = stack.pop()
        print(node.val)
        tempNode = node.right

# 后序遍历
def latOrderStack(root):
    if root == None:
        return None
    stack = []
    tempNode = root
    while tempNode or stack:
        while tempNode:
            stack.append(tempNode)
            tempNode = tempNode.left
    
        node = stack[-1]
        tempNode = node.right
        if tempNode == None:
            print(node.val)
            node = stack.pop()
            while stack and node == stack[-1].right:
                node = stack.pop()
                print(node.val)

# 先序遍历v2
def preOrderStackv2(root):
    if root == None:
        return None
    stack = []
    tempNode = root

    while stack or tempNode:
        if tempNode:
            print(tempNode.val)
            stack.append(tempNode)
            tempNode = tempNode.left
        else:
            node = stack.pop()
            tempNode = node.right

# 中序遍历v2
def midOrderStackv2(root):
    if root == None:
        return None
    stack = []
    tempNode = root

    while stack or tempNode:
        if tempNode:
            stack.append(tempNode)
            tempNode = tempNode.left
        else:
            node = stack.pop()
            print(node.val)
            tempNode = node.right

# 后序遍历v2
def latOrderStackv2(root):
    if root == None:
        return None
    stack = []
    tempNode = root

    while stack or tempNode:
        if tempNode:
            stack.append(tempNode)
            tempNode = tempNode.left
        else:
            node = stack[-1]
            tempNode = node.right
            if tempNode == None:
                print(node.val)
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
                    print(node.val)


# 广度优先搜索

def BreadthFirstSearch(root):
    if root == None:
        return []
    
    nodeList = [root]
    result = [root.val]

    while nodeList:
        currentNode = nodeList.pop(0)

        if currentNode.left:
            nodeList.append(currentNode.left)
            result.append(currentNode.left.val)
        
        if currentNode.right:
            nodeList.append(currentNode.right)
            result.append(currentNode.right.val)
    
    return result

'''
            t1
         /      \
       t2       t3
      /  \     /  \
    t4    t5  t6   t7 
                \
                 t8
'''

if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8
    
    # preOrderRecursive(t1)
    # print('-'*30)
    # midOrderRecursive(t1)
    # print('-'*30)
    # latOrderRecursive(t1)
    # print('-'*30)

    preOrderStack(t1)
    print('-'*30)
    midOrderStack(t1)
    print('-'*30)
    latOrderStack(t1)
    print('-'*30)

    preOrderStackv2(t1)
    print('-'*30)
    midOrderStackv2(t1)
    print('-'*30)
    latOrderStackv2(t1)
    print('-'*30)
    print(BreadthFirstSearch(t1))
