import os
import os.path

DB_NAME = 'Task.db'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, DB_NAME)

SERVER_PORT = 8080

# response codes
ERROR_RESOURCE_NOT_FOUND = 401
ERROR_RESOURCE_ALREADY_EXISTS = 409
ERROR_BAD_REQEUST = 400
SUCCESS_RESPONSE = 201