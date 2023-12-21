from flask import Flask, request, render_template   

app = Flask(__name__) 

todos = ["Get Money", "Get Paper"] 

@app.route('/', methods =['GET','POST']) 

def index():  
    new_todo = request.form['new_todo']
    return render_template('todo.html.jinja', todos=todos )
