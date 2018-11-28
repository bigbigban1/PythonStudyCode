"""
输入某年某月某日，判断这一天是这一年的第几天？
"""

year=int(input('请输入年:'))
month=int(input('请输入月:'))
day=int(input('请输入天:'))
sum=day
days = [31,28,31,30,31,30,31,31,30,31,30,31]
i=0
if ( year%4 == 0 and year%100 != 0) or (year%400 == 0):
    days[1] = 29
while i< month-1:
    sum=sum+days[i]
    i+=1
print('这一天是该年的第',sum,'天')