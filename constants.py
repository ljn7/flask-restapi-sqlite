import os
import os.path

# setting up database uri
DB_NAME = 'user.db'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, DB_NAME)

SERVER_PORT = 8080