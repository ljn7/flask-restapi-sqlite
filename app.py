from start import *
from db import Tasks, TasksSchema, tasks_schema
from constants import *
from commands import *

@app.route('/')
def welcome():
    return """<pre>Available routes:
                /task/{id}
                /task/create?title='String'&description='String'&due_date='String'&status='String'
                /task/updatebyid?id='Number'&title='String'&description='String'&due_date='String'&status='String'
                /task/deletebyid?id='Number'
                /tasks
                Note:
                To send forward slashes on due date from url query using %2F instead / 
                    for example 01%2F01%2F2023 instead of 01/01/2023</pre>
    """

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        tasks_paginated = Tasks.query.paginate(page=page, per_page=per_page)
        tasks_list = tasks_paginated.items
        total_pages = tasks_paginated.pages
        result = tasks_schema.dump(tasks_list)
        return jsonify(data=result, total_pages=total_pages), SUCCESS_RESPONSE
    except BaseException as error:
        print(error)
        return jsonify("Internal server error"), ERROR_INTERNAL_SERVER

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id: int):
    try:
        task = Tasks.query.filter_by(id=task_id).first()
        if task is not None:
            result = tasks_schema.dump([task])
            return jsonify(result[0]), SUCCESS_RESPONSE

        return jsonify(message="Task doesn't exists"), ERROR_RESOURCE_NOT_FOUND
    except BaseException as error:
        print(error)
        return jsonify("Internal server error"), ERROR_INTERNAL_SERVER


@app.route('/task/create', methods=['POST'])
def create_task():
    try:
        form = request.form
        title = form('title')
        desc = form('description')
        due_date = form('due_date')
        status = form('status')

        if None not in (title, desc, due_date, status) and title != "":
            task = Tasks.query.filter_by(title=title).first()

            if task:
                return jsonify(message="There is a task already having that title"), ERROR_RESOURCE_ALREADY_EXISTS
            
            if status not in ['Incomplete', 'In Progress', 'Completed']:
                return jsonify(message="Bad request (check status value)"), ERROR_BAD_REQUEST
                    
            new_task = Tasks(title=title,
                            description=desc,
                            due_date=due_date,
                            status=status)
            db.session.add(new_task)
            db.session.commit()

            return jsonify(message="Adding a task was successful!"), SUCCESS_RESPONSE

        return jsonify(message="Adding a task was unsuccessful"), ERROR_BAD_REQUEST
    except BaseException as error:
        print(error)
        return jsonify("Internal server error"), ERROR_INTERNAL_SERVER

@app.route('/task/update', methods=['PUT'])
def update_task():
    try:
        form = request.form
        task_id = int(form('id'))
        task = Tasks.query.filter_by(id=task_id).first()

        if task is None:
            return jsonify(message="Task wasn't found with given id"), ERROR_RESOURCE_NOT_FOUND
        
        title = form('title')
        desc = form('descripton')
        due_date = form('due_date')
        status = form('status')

        if title is not None and title != "":
            task.title = title
        if desc is not None and desc != "":
            task.description = desc
        if due_date is not None and due_date != "":
            task.due_date = due_date
        if status is not None and status != "":
            if status in ['Incomplete', 'In Progress', 'Completed']:
                task.status = status
            else:
                return jsonify(message="Bad request (check status value)"), ERROR_BAD_REQUEST
            
        db.session.commit()
        return jsonify(message="Updated the task"), SUCCESS_RESPONSE
    except BaseException as error:
        print(error)
        return jsonify("Internal server error"), ERROR_INTERNAL_SERVER

@app.route('/task/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id: int):
    try:
        task = Tasks.query.filter_by(id=task_id).first()
        if task:
            db.session.delete(task)
            db.session.commit()
            return jsonify(message="Task has been deleted successfully"), SUCCESS_RESPONSE
        return jsonify(message="Task doesn't exists"), ERROR_RESOURCE_NOT_FOUND
    except BaseException as error:
        print(error)
        return jsonify("Internal server error"), ERROR_INTERNAL_SERVER

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=SERVER_PORT, debug=True)
