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

def get_todos():
    with conn.cursor() as cursor:
        cursor.execute("SELECT `description` FROM `Todos`")
        results = cursor.fetchall()
        todos = [item['description'] for item in results]
    return todos

@app.route('/', methods=['GET', 'POST'])
def index():
    todos = get_todos()

    if request.method == 'POST':
        new_todo = request.form['new_todo']
        with conn.cursor() as cursor:
            cursor.execute(f"INSERT INTO `Todos` (`description`) VALUES ('{new_todo}')")
        conn.commit()
        todos = get_todos()

    return render_template('todo.html.jinja', todos=todos)

@app.route('/delete_todos/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    todos = get_todos()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM `Todos` WHERE `description` = %s", (todos[todo_index],))
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
