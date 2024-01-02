from flask import Flask, request, render_template, redirect   

app = Flask(__name__) 

todos = ["Get Money", "Get Paper"] 

@app.route('/', methods =['GET','POST']) 

def index():  
    if request.method=='POST': 
        new_todo = request.form['new_todo'] 
        todos.append(new_todo)
    return render_template('todo.html.jinja', todos=todos ) 

@app.route('/delete_todos/<int:todo_index>', methods= ['POST']) 
def todo_delete(todo_index): 
    del todos[todo_index] 

    return redirect('/')