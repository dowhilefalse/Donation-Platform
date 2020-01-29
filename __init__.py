from flask import Flask, request, url_for, redirect, render_template
import os
app = Flask(__name__, static_folder='static')

import pymysql


conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0413',
    db='charity_forms',
    charset='utf8'
)

# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('contact.html')


@app.route('/registerform', methods=['GET', 'POST'])
def registerform(): 
    cursor = conn.cursor()
    # SQL 插入语句
    sql = "INSERT INTO account (user, password, email) VALUES ("+request.args.get('user')+", "+request.args.get('password')+", "+request.args.get('email')+")"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
         #注册成功之后跳转到登录页面
        return render_template('contact.html') 
    except:
        #抛出错误信息
        traceback.print_exc()
        # 如果发生错误则回滚
        dconn.rollback()
        return '注册失败'
    # 关闭数据库连接
    cursor.close()

    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('index'))  
    return render_template('register.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('about.html')

@app.route('/group1', methods=['GET', 'POST'])
def group1():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('group1.html')


@app.route('/group2', methods=['GET', 'POST'])
def group2():
    if request.method == 'POST':
        return redirect(url_for('index'))    
    cur = conn.cursor()

    # get annual sales rank
    sql = "select * from 全国"
    cur.execute(sql)
    content = list(cur.fetchall())
    
    new_content = []
    for i in range(len(content)):
        if content[i][0] is None:
            content = content[:i]
            break
        else:
            new_content.append(list(content[i]))
    for i in range(len(new_content)):
        for j in range(len(new_content[i])):
            new_content[i][j] = str(new_content[i][j])
        

	# 获取表头
    sql = "SHOW FIELDS FROM 全国"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    cur.close()
    return render_template('group2.html', labels=labels, content=new_content)

@app.route('/group11', methods=['GET', 'POST'])
def group11():
    if request.method == 'POST':
        return redirect(url_for('index'))
    
    cur = conn.cursor()

    # get annual sales rank
    sql = "select * from 武汉"
    cur.execute(sql)
    content = list(cur.fetchall())
    
    new_content = []
    for i in range(len(content)):
        if content[i][0] is None:
            content = content[:i]
            break
        else:
            new_content.append(list(content[i]))
    for i in range(len(new_content)):
        for j in range(len(new_content[i])):
            new_content[i][j] = str(new_content[i][j])
        

	# 获取表头
    sql = "SHOW FIELDS FROM 武汉"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    cur.close()
    return render_template('group11.html', labels=labels, content=new_content)

@app.route('/group12', methods=['GET', 'POST'])
def group12():
    if request.method == 'POST':
        return redirect(url_for('index'))
    
    cur = conn.cursor()

    # get annual sales rank
    sql = "select * from 武汉周边"
    cur.execute(sql)
    content = list(cur.fetchall())
    
    new_content = []
    for i in range(len(content)):
        if content[i][0] is None:
            content = content[:i]
            break
        else:
            new_content.append(list(content[i]))
    for i in range(len(new_content)):
        for j in range(len(new_content[i])):
            new_content[i][j] = str(new_content[i][j])
        

	# 获取表头
    sql = "SHOW FIELDS FROM 武汉周边"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    cur.close()
    return render_template('group12.html', labels=labels, content=new_content)
#     return render_template('group12.html')

if __name__ == "__main__":
    app.run()