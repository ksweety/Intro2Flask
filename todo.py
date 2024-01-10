from flask import Flask, request, render_template, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)

conn = pymysql.connect(host='10.100.33.60',
                      user='kwilliams4',
                      password='228426581',
                      database='kwilliams4_todo',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

# ...

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        new_todo = request.form['new_todo']
        with conn.cursor() as cursor:
            cursor.execute(f"INSERT INTO `Todos` (`description`) VALUES ('{new_todo}')")

        conn.commit()
    
    cursor = conn.cursor()
    cursor.execute("SELECT * from `Todos` ORDER BY `completions`")
    results = cursor.fetchall() 
    cursor.close()

   
    return render_template('todo.html.jinja', todos=results)

@app.route('/delete_todos/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM `Todos` WHERE `id` = {todo_index}")
    conn.commit()

    return redirect('/') 

@app.route('/complete_todos/<int:todo_index>', methods=['POST'])
def complete_todo(todo_index):
    with conn.cursor() as cursor:
        cursor.execute(f"UPDATE `Todos` SET `completions` = 1 WHERE `id` = {todo_index}")
    conn.commit()

    return redirect('/')
