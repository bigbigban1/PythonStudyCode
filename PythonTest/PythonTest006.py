"""
斐波那契数列。
"""

i = int(input("需要输出多少个斐波拉契数列："))

def fib(i):
    a,b = 1,1
    for n in range(0,n):
        a,b = b.a+b
    return a

print(fib(i))