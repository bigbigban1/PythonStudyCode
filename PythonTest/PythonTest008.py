# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

i=987

while i<=999:
    a = (i // 100)**3
    b = (i % 10)**3
    c = (i // 10 % 10)**3
    if i==a+b+c:
        print(i)
    i+=1
