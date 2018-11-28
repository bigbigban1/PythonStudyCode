# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def FindMaxAndMin(L):
    if len(L)==0:
            return (None,None)
    max = L[0]
    min = L[0]
    for i in L:
        if i>max:
            max = L[i]
        if i<min:
            min = L[min]
    return (max,min)

l = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
n = []
print(FindMaxAndMin(l))
print(FindMaxAndMin(n))

# (-1, -9)
# (None, None)
