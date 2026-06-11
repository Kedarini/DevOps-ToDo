from flask import Flask, render_template_string, request, redirect, abort

app = Flask(__name__)

todos = ["Buy milk", "Run Docker"]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps ToDo</title>
</head>
<body>
    <h1>Moja Lista ToDo (Nginx)</h1>

    <form action="/add" method="POST">
        <input type="text" name="task" placeholder="New task" required>
        <button type="submit">Dodaj</button>
    </form>

    <form action="/remove" method="POST">
    <ul>
        {% for todo in todos %}
            <li> 
                {{ todo }} 
                <button type="submit" name="todo" value="{{ todo }}">Remove</button> 
            </li>
        {% endfor %}
    </ul>
</form>

    <hr>
    <p>Strefa Testowa DevOps:</p>
    <a href="/break" style="color: red;">Return Error 500 (Internal Server Error)</a>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        todos.append(task)
    return redirect('/')

@app.route('/remove', methods=['POST'])
def remove_todo():
    remove_task = request.form.get('todo')
    if remove_task in todos:
        todos.remove(remove_task)
    return redirect('/')

@app.route('/break')
def breaking():
    abort(500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)