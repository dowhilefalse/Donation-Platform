from flask import Flask, request, url_for, redirect, render_template
import os
app = Flask(__name__)

import pymysql


conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0413',
    db='charity_forms',
    charset='utf8'
)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('contact.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('about.html')

@app.route('/group2', methods=['GET', 'POST'])
def group2():
    if request.method == 'POST':
        return redirect(url_for('index'))    
    cur = conn.cursor()

    # get annual sales rank
    sql = "select * from 武汉"
    cur.execute(sql)
    content = list(cur.fetchall())
    
    for i in range(len(content)):
#     print(contents[i][0])
        if content[i][0] is None:
            content = content[:i]
            break

	# 获取表头
    sql = "SHOW FIELDS FROM 全国"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    cur.close()
    return render_template('group2.html', labels=labels, content=content)

@app.route('/group11', methods=['GET', 'POST'])
def group11():
    if request.method == 'POST':
        return redirect(url_for('index'))
    
    cur = conn.cursor()

    # get annual sales rank
    sql = "select * from 武汉"
    cur.execute(sql)
    content = list(cur.fetchall())
    
    for i in range(len(content)):
#     print(contents[i][0])
        if content[i][0] is None:
            content = content[:i]
            break

	# 获取表头
    sql = "SHOW FIELDS FROM 武汉"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    cur.close()
    return render_template('group11.html', labels=labels, content=content)

@app.route('/group12', methods=['GET', 'POST'])
def group12():
    if request.method == 'POST':
        return redirect(url_for('index'))
    
        cur = conn.cursor()

    # get annual sales rank
    sql = "select * from 武汉"
    cur.execute(sql)
    content = list(cur.fetchall())
    
    for i in range(len(content)):
#     print(contents[i][0])
        if content[i][0] is None:
            content = content[:i]
            break

	# 获取表头
    sql = "SHOW FIELDS FROM 武汉周边"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    cur.close()
    return render_template('group12.html', labels=labels, content=content)
#     return render_template('group12.html')

if __name__ == "__main__":
    app.run()