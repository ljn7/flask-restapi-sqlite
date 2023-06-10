import os
import os.path

# setting up database uri
DB_NAME = 'user.db'
BASE_URI = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, db_name)

SERVER_PORT = 8080