# 类的访问限制练习代码
class Student():
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def set_sore(self,score):#进行参数检查
        if not isinstance(score,int):
            raise ValueError('Score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('Score must in 0~100!')
        self.__score = score

    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score
    def get_name(self):
        return self.__name

st = Student('Jack',50)
print(st.get_name())
print(st.get_score())
st.set_name('Marry')
st.set_sore(80)
print(st.get_name())
print(st.get_score())