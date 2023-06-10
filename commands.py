from start import *
from db import Tasks

@app.cli.command('db.create')
def db_create():
    db.create_all()
    print('Database created successfully!')


@app.cli.command('db.drop')
def db_drop():
    db.drop_all()
    print('Database dropped successfully!')

@app.cli.command('db.seed')
def db_seed():

    task1 = Tasks(title='Backend',
                  description='Backend Intern task',
                  due_date='11/06/2023',
                  status='In Progress')
    
    task2 = Tasks(title='Getting hired',
                  description='Would I get hired?',
                  due_date='**/**/2023',
                  status='In Progress')
    
    db.session.add(task1)
    db.session.add(task2)

    test_task = Tasks(title='Test',
                      description='Test desc',
                      due_date='01/01/2023',
                      status='Completed')
    
    db.session.add(test_task)

    db.session.commit()
    print("Database seeding completed")