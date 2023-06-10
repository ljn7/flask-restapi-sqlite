from start import *

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    due_date = Column(String)
    status = Column(String)

    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status


class TasksSchema(ma.Schema):
    
    class Meta:
        fields = ('id', 'title', 'description', 'due_date', 'status')


tasks_schema = TasksSchema(many=True)