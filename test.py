a = [1, 2, 3]

def aaa(a):
    a.append(4)

# print(a)
# aaa(a)
# print(a)

# for i in range(3, 0, -1):
#     print(i)

# result = [-1]
# result += [1,2,3]
# print(result)

numbers = [9,8,7,6,5]
numbers = list(map(str, numbers))
print(''.join(numbers))

# 字典排序
# a = {'a':2, 'b':1}
# # print(a.items())
# # print('a' in a)
# b = sorted(a.items(), key=lambda x: x[1])
# print(b)

# a = 'abcded'
# print(a.index('d'))
# print(a.count('d'))

# cc = [1, 2, 1, 3, 1]
# print(cc.count(1))

# a = 'abcded'
# b = 'cdfg'
# a = list(a)
# b = list(b)
# b[0] = a[0]
# print(''.join(b))

# print(ord('A'))
# print(ord('Z'))

a = [1, 2, 1, 3, 5]
# print(a.split(' ')[::-1])
print(a[5:])

# a1 = '1234'
# t = 2
# if a1[0] > '0' and a1[0] < '1':
#     print(type(a1[0]))

# print(-0x80000000)
# print(list('a'))
a = ['a']
a.pop()
# print(max([]))

print(sum(map(int, list('123'))))