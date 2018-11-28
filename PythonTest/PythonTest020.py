#实例属性和类属性学习代码，还存在疑问
class Animal():
    count = 0
    def __init__(self):
        Animal.count+=1

a = Animal()
b = Animal()
c = Animal()
d = Animal()
print(a.count)
print(b.count)
print(c.count)
print(d.count)
print(Animal().count)
print(Animal().count)
print(Animal().count)
print(Animal().count)
