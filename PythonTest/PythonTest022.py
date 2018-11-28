#定制类学习代码
class Student(object):
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return 'Student object (name:%s)'%self._name
    __repr__ = __str__
st = Student('Jack')

class Animal(object):
    def __init__(self,name,limb,Father):
        self._name = name
        self.limb = limb
        self._father = Father
    def __str__(self):
        return 'Animal called %s,running with %d limbs,father is %s'%(self._name,self.limb,self._father)
    __repr__ = __str__

monkey = Animal('Monkey',2,'Monkeyyyy')
print(monkey)