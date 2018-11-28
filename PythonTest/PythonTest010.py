# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

letter=[]
space=[]
number=[]
other=[]

str=input("请输入字符串")

for i in range(0,len(str)):
    if str[i].isalpha():
        letter.append(str[i])
    elif str[i].isspace():
        space.append(str[i])
    elif str[i].isalnum():
        number.append(str[i])
    else:
        other.append(str[i])
print("letter=%d,space=%d,number=%d,other=%d"%(len(letter),len(space),len(number),len(other)))
print(letter)
print(space)
print(number)
print(other)