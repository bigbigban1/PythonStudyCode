"""
输入三个整数x,y,z，请把这三个数由小到大输出。
"""

Number = []

for i in range(0,3):
    x = int(input())
    Number.append(x)

Number.sort(reverse= True)
print(Number)
