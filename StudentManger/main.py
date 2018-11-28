import pymysql

dictMenu = {1:"增加",2:"删除",3:"修改",4:"查看"}
#修改user为你的mysql用户名，password为你的mysql密码，db为你创建的数据库，port为你的mysql端口，不知道怎么看端口的百度
db= pymysql.connect(host="localhost",user="root",password="2355",db="pythontest1",port=3306)
cur = db.cursor()

def lookup():
    sql = 'select * from studentInfo'
    cur.execute(sql)  # 执行sql语句
    results = cur.fetchall()  # 获取查询的所有记录
    print("NAME\t\t\t", "ID\t\t\t", "ADDRESS\t","SEX\t\t")
    print('*****************************')
    # 遍历结果
    for row in results:
        name = row[0]
        id = row[1]
        address = row[2]
        sex = row[3]
        print('%s\t'%name,'%s\t'%id,'%s\t'%address,'%s\t'%sex)

def insert():
    name = input("请输入姓名：")
    id = input("请输入学号：")
    address = input("请输入地址：")
    sex = input("请输入性别：")
    try:
        cur.execute("insert into studentInfo values('%s','%s','%s','%s')"%(name,id,address,sex))
        print("插入成功！")
    except BaseException:
        print("数据异常！")
    lookup()

def delete():
    dele = int(input("请选择删除的属性，1：姓名，2：学号，3：地址，4：性别\n"))
    deleter = input("请输入要删除的属性：\n")
    if dele < 1 or dele > 4:
        raise ValueError('输入错误！')
    if dele == 1:
        cur.execute("delete from studentInfo where name = '%s'"%deleter)
    elif dele == 2:
        # int(deleter)
        cur.execute("delete from studentInfo where id = '%d'" % int(deleter))
    elif dele == 3:
        cur.execute("delete from studentInfo where address = '%s'" % deleter)
    elif dele == 4:
        cur.execute("delete from studentInfo where sex = '%s'" % deleter)
    lookup()

def change():
    changer_no1 = int(input("请输入要修改的学生的学号："))
    print("该学生信息为：")
    cur.execute("select * from studentInfo where id = '%d'"%changer_no1)
    result = cur.fetchall()
    print(result)
    changer_no2 = 0
    try:
        changer_no2 = int(input("请选择要修改的项目：1：姓名，2：学号，3：地址，4：性别"))
    except BaseException:
        print('输入错误！')
    if changer_no2 < 1 or changer_no2 > 4:
        raise ValueError('输入错误！')
    changer_no3 = input("请输入要修改的属性值：")
    if changer_no2 == 1:
        cur.execute("UPDATE studentInfo SET name = '%s' WHERE id = '%d'"%(changer_no3,changer_no1))
    elif changer_no2 == 2:
        cur.execute("UPDATE studentInfo SET id = '%d' WHERE id = '%d'"%(int(changer_no3),changer_no1))
    elif changer_no2 == 3:
        cur.execute("UPDATE studentInfo SET address = '%s' WHERE id = '%d'"%(changer_no3,changer_no1))
    elif changer_no2 == 4:
        cur.execute("UPDATE studentInfo SET sex = '%s' WHERE id = '%d'"%(changer_no3,changer_no1))
    lookup()

choose = 0
try:
    choose = int(input("输入数字来进行选择，1：增加，2：删除，3：修改，4：查看"))
except BaseException:
    print('输入错误！')
if not isinstance(choose,int) or choose < 1 or choose > 4:
    raise ValueError('输入错误！')
print("选择%s"%dictMenu[choose])
if choose == 1:
    insert()
elif choose ==2:
    delete()
elif choose == 3:
    change()
elif choose == 4:
    lookup()