# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

num = int(input("请输入相加的数字："))
add = int(input("请输入相加的次数："))
total = 0

for i in range(0,add):
    total+=num
    num = num*10+num

print(total)