import os
import os.path

DB_NAME = 'Task.db'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, DB_NAME)

SERVER_PORT = 8080