import hashlib

SHA = hashlib.sha256()

class User_Login(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def Hash(self):
        user_info = '%s%s'%(self.username,self.password)
        SHA.update(user_info.encode('utf-8'))
        return SHA.hexdigest()

user_name = str(input('请输入账号：'))
user_pwd = str(input('请输入密码:'))

user1 = User_Login(user_name,user_pwd)
print(user1.Hash())
