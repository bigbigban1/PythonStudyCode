import pymysql
#数据库连接信息，host为mysql地址，默认为localhost，user为mysql用户，password为密码，由于涉及中文，请手工创建angui数据库
#create database angui DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
try:
	conn = pymysql.connect(
	    host="localhost",
	    user="root",
	    password="root",
	    database="mysql",
	)
except BaseException:
	print("数据库连接失败")
	exit(0)

cursor = conn.cursor()
def create_database_angui():
	print("正在创建数据库angui")
	sql = "create database angui"
	cursor.execute(sql)
	conn.commit()
	print("angui数据库创建完毕")
	sql = "use angui"
	cursor.execute(sql)
	conn.commit()

def create_charge_database():
	print("正在创建判断题表")
	sql = """create table charge(
	question_id VARCHAR(4) NOT NULL,
	question_type VARCHAR(20) NOT NULL,
	question_stem VARCHAR(100) NOT NULL,
	question_score VARCHAR(4) NOT NULL,
	answer_true VARCHAR(4) NOT NULL,
	PRIMARY KEY ( question_id )
	) DEFAULT CHARSET=utf8"""
	cursor.execute(sql)
	f = open(r"../Question_bank/charge.txt","r",encoding="utf-8")
	for line in f.readlines():
		line_list = line.split(".")
		sql = 'insert into charge values("{}","{}","{}","{}","{}")'.format(
			line_list[0],
			line_list[1],
			line_list[2],
			line_list[3],
			line_list[4],
		)
		cursor.execute(sql)
	conn.commit()
	print("判断题表创建完毕")

def create_choose_database():
	print("正在创建选择题表")
	sql = """create table choose(
	question_id VARCHAR(4) NOT NULL,
	question_type VARCHAR(20) NOT NULL,
	question_stem VARCHAR(100) NOT NULL,
	question_score VARCHAR(4) NOT NULL,
	answer_true VARCHAR(4) NOT NULL,
	answer_a VARCHAR(100) NOT NULL,
	answer_b VARCHAR(100) NOT NULL,
	answer_c VARCHAR(100) NOT NULL,
	answer_d VARCHAR(100) NOT NULL,
	PRIMARY KEY ( question_id )
	) DEFAULT CHARSET=utf8
	"""
	cursor.execute(sql)
	f = open(r"../Question_bank/choose.txt","r",encoding="utf-8")
	for line in f.readlines():
		line_list = line.split(".")
		sql = 'insert into choose values("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
			line_list[0],
			line_list[1],
			line_list[2],
			line_list[3],
			line_list[4],
			line_list[5],
			line_list[6],
			line_list[7],
			line_list[8],
		)
		cursor.execute(sql)
	conn.commit()
	print("选择题数据表创建完毕")

try:
	create_database_angui()
except BaseException:
	print("安规数据库已存在，请先删除再创建")
	exit(0)

try:
	create_choose_database()
	create_charge_database()
except pymysql.err.InternalError:
	print("charge表或choose表已存在，请先删除再创建")
	exit(0)