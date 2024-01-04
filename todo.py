from flask import Flask, request, render_template, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)


con = pymysql.connect(host='10.100.33.60',
                      user='kwilliams4',
                      password='228426581',
                      database='world',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods=['GET', 'POST'])
def index():
  
    with con.cursor() as cursor:
        cursor.execute("SELECT `description` FROM `todos`")
        results = cursor.fetchall()
        todos = results

    if request.method == 'POST':
        new_todo = request.form['new_todo']
    
        with con.cursor() as cursor:
            cursor.execute("INSERT INTO `todos` (`description`) VALUES (%s)", (new_todo,))
            con.commit()

    return render_template('todo.html.jinja', todos=todos)

@app.route('/delete_todos/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
   
    with con.cursor() as cursor:
        cursor.execute("DELETE FROM `todos` WHERE `description` = %s", (todos[todo_index]['description'],))
        con.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
