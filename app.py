# from flask import Flask, request, Response, jsonify
from start import *
from db import Tasks, TasksSchema, tasks_schema
from constants import *
from commands import *

# app = Flask(__name__)


@app.route('/')
def welcome():
    return """<pre>Available routes:
                /task/{id}
                /task/create?title='String'&description='String'&due_date='String'&status='String'
                /task/updatebyid?id='Number'&title='String'&description='String'&due_date='String'&status='String'
                /task/deletebyid?id='Number'
                /tasks</pre>
    """

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    print("Fetching all the tasks...")
    tasks_list = Tasks.query.all()
    result = tasks_schema.dump(tasks_list)
    return jsonify(data=result)

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id: int):
    task = Tasks.query.filter_by(id=task_id).first()

    if task is not None:
        result = TasksSchema.dump(task)
        return jsonify(result)

    return jsonify(message="Task doesn't exists"), ERROR_RESOURCE_NOT_FOUND


@app.route('/task/create', methods=['GET'])
def create_task():

    args = request.args
    title = args.get('title')
    desc = args.get('description')
    due_date = args.get('due_date')
    status = args.get('status')

    if None not in (title, desc, due_date, status):
        task = Tasks.query.filter_by(title=title).first()

        if task:
            return jsonify("There is a task already by that name"), ERROR_RESOURCE_ALREADY_EXISTS

        new_task = Tasks(title=title,
                         description=desc,
                         due_date=due_date,
                         status=status)
        db.session.add(new_task)
        db.session.commit()

        return jsonify(message="Adding a task was successful!"), SUCCESS_RESPONSE

    return jsonify(message='Adding a task was unsuccessful'), ERROR_BAD_REQEUST


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=SERVER_PORT, debug=True)
