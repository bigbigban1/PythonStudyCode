#类的继承和态学习代码
import functools
from prn_obj import prn_obj

def createNote(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("A new example has been setted!")
        return func(*args,**kw)
    return wrapper

class Animal(object):
    @createNote
    def __init__(self,name,limbNum):
        self.name = name
        self.__limbNum = limbNum
    def getName(self):
        print(self.name)
    def getLimgNum(self):
        return self.__limbNum
    def run(self):
        print("Animal is running with %s limbs!"%self.__limbNum)

class Dog(Animal):
    def run(self):
        print("Dog is running with %s limbs!" % self.getLimgNum())

class Cat(Animal):
    def run(self):
        print("Cat is running with %s limbs!" % self.getLimgNum())

def runTwice(animal):
    animal.run()
    animal.run()

dog = Dog('amny',4)
cat = Cat('putty',4)
dog.run()
cat.run()

runTwice(Animal('animal',4))
print('')
runTwice(Dog('amny',4))
print('')
runTwice(Cat('putty',4))