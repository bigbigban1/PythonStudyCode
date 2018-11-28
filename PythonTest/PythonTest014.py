#实现字符串转化为数字（仅限全为数字的字符串）
from functools import reduce

Dict={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',}

x = 123456789

def change(x):
     L = []
     while x>9:
         L.insert(0,x%10)
         x = x//10
     L.insert(0,x)
     return L
L = change(x)
s=''
for n in L:
    s = s+Dict[n]
print(s)


# map : 讲后面的元素全部作为前面函数的参数
# reduce ：将后面元素的每一个作为前面函数的参数运算后又参与到下一个元素的运算中

# map 返回的是一个生成器，需要用next()或者for循环来遍历
# reduce返回的是一个值，也许是数字也许是字符串

