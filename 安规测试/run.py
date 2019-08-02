import pymysql
import random
import os
from Setup import answer_list


choose_answer_list = answer_list.get_answer_list()
charge_answer_list = ['A','B']

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="angui",
)

cursor = conn.cursor()

i = 0
while True:
	j = random.randint(1,515)
	if j>=1 and j<=353:
		question = 'select question_stem,answer_a,answer_b,answer_c,answer_d,question_type,answer_true from choose where question_id = "{}"'.format(j)
		cursor.execute(question)
		tup = cursor.fetchone()
		print("{5}:{0}\nA.{1}\nB.{2}\nC.{3}\nD.{4}".format(tup[0],tup[1],tup[2],tup[3],tup[4],tup[5]),end="")
		user_answer = input("请输入你的选项(可使用QWER替代ABCD)\n")
		user_answer = user_answer.upper()
		user_answer = user_answer.replace("Q","A").replace("W","B").replace("E","C").replace("R","D")
		true_set = set(tup[6])
		user_set = set(user_answer)
		print("你选择：{}，正确答案是:{}".format(user_answer,tup[6]))
		if user_answer not in choose_answer_list:
			print("回答错误")
		else:
			if user_set == true_set:
				print("回答正确")
			else:
				print("回答错误")
	else:
		question = 'select question_stem,question_type,answer_true from charge where question_id = "{}"'.format(j)
		cursor.execute(question)
		tup = cursor.fetchone()
		print("{}:{}\n".format(tup[1], tup[0]),end="")
		user_answer = input("A为正确，B为错误，请选择（可使用QW替代AB）:\n")
		user_answer = user_answer.upper()
		user_answer = user_answer.replace("Q", "A").replace("W", "B").replace("E", "C").replace("R", "D")
		true_answer = tup[2]
		true_answer = true_answer.replace("\r\n","").replace("\r","").replace("\n","")
		print("你的选择是：{}，正确答案是：{}".format(user_answer,true_answer))
		if user_answer not in charge_answer_list:
			print("回答错误")
		else:
			if user_answer == true_answer:
				print("回答正确")
			else:
				print("回答错误")
	i = i+1
	if i>100:
		exit()
	input("请按回车继续")
	os.system("cls")
cursor.close()