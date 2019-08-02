from flask import Flask, render_template, request, session, redirect, url_for
import config
import pymysql
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This_is_for_anTICsRf'
app.secret_key = 'This_is_for_anTICsRf'

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="angui",
)

cursor = conn.cursor()

@app.route('/',methods=['GET','POST'])
def get_question():
    if request.method == "GET":
        i = random.randint(1,515)
        if i >=1 and i<=219:
            question = 'select question_stem,answer_a,answer_b,answer_c,answer_d,question_type,answer_true from choose where question_id = "{}"'.format(i)
            cursor.execute(question)
            tup = cursor.fetchone()
            question_information = {
                'question_id':i,
                'question_stem':tup[0],
                'answer_a':tup[1],
                'answer_b':tup[2],
                'answer_c':tup[3],
                'answer_d':tup[4],
                'question_type':tup[5],
                'answer_true':tup[6],
            }
            return render_template('choose.html', **question_information)
        elif i>219 and i <=353:
            question = 'select question_stem,answer_a,answer_b,answer_c,answer_d,question_type,answer_true from choose where question_id = "{}"'.format(
                i)
            cursor.execute(question)
            tup = cursor.fetchone()
            question_information = {
                'question_id': i,
                'question_stem': tup[0],
                'answer_a': tup[1],
                'answer_b': tup[2],
                'answer_c': tup[3],
                'answer_d': tup[4],
                'question_type': tup[5],
                'answer_true': tup[6],
            }
            return render_template('choose_single.html', **question_information)
        else:
            question = 'select question_stem,question_type,answer_true from charge where question_id = "{}"'.format(i)
            cursor.execute(question)
            tup = cursor.fetchone()
            question_information = {
                'question_stem':tup[0],
                'question_type':tup[1],
                'answer_true':tup[2],
                'question_id':i,
            }
            return render_template('charge.html',**question_information)
    elif request.method == "POST":
        chcarge_dict = {"A":"正确","B":"错误"}
        questionID = request.values['questionID']
        questionID = int(questionID)
        answer = ""
        answer_list = request.values.getlist("answer")
        for item in answer_list:
            answer = answer+item
        answer = str(answer)
        if questionID>=1 and questionID<=353:
            sql = 'select answer_true from choose where question_id={}'.format(questionID)
            cursor.execute(sql)
            answer_true = cursor.fetchone()
            answer_true = str(answer_true[0])
            answer_true = answer_true.replace("\n","").replace("\\","").replace("\\n","").replace("n","")
            if answer_true == answer:
                response = {
                    "result": "回答正确",
                }
                return render_template('result.html',**response)
            else:
                response = {
                    "result": "回答错误，正确答案为:{}".format(answer_true)
                }
                return render_template('result.html', **response)
        else:
            sql = 'select answer_true from charge where question_id={}'.format(questionID)
            cursor.execute(sql)
            answer_true=cursor.fetchone()
            answer_true = str(answer_true[0])
            answer_true = answer_true.replace("\n","").replace("\\","").replace("\\n","").replace("n","")
            if answer_true == answer:
                response = {
                    "result" : "回答正确",
                }
                return render_template('result.html', **response)
            else:
                response = {
                    "result": "回答错误，正确答案为:{}".format(answer_true)
                }
                return render_template('result.html', **response)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")