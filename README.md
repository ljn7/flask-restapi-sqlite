# Backend Intern Test

This project is a RESTful API built with Python, utilizing Flask and SQLite, for managing tasks. The API provides endpoints for creating, retrieving, updating, and deleting tasks. Pagination is also supported for retrieving tasks in a paginated manner.

## Build using Docker

To build the project using Docker, navigate to the current directory and run the following command:

```bash
docker build -t <tag-name> .
```

## Run using Docker

To run the project using Docker, use the following command:

```bash
docker run -p 8080:8080 <name-of-the-built-image>
```

## Base URL

The default base URL is:

```
http://localhost:8080
```

## Available Routes

- `/task/{id}`
- `/task/create`
- `/task/update`
- `/task/delete/{task_id}`
- `/tasks`

## API Endpoints

### Welcome

Displays the available routes.

**Endpoint**: `/`

**Method**: GET

**Response**

- Status Code: 200 (OK)
- Body:
```json
{
    "routes": [
        {
            "url": "/task/{id}",
            "description": "Retrieve a specific task by ID."
        },
        {
            "url": "/task/create",
            "description": "Create a new task."
        },
        {
            "url": "/task/updatebyid",
            "description": "Update a task by ID."
        },
        {
            "url": "/task/deletebyid?id={int: id}",
            "description": "Delete a task by ID."
        },
        {
            "url": "/tasks",
            "description": "Retrieve all tasks with pagination support."
        }
    ]
}
```

### Get All Tasks

Retrieves all tasks with pagination support.

**Endpoint**: `/tasks`

**Method**: GET

**Parameters**:

- `page` (optional): The page number to retrieve (default: 1).
- `per_page` (optional): The number of tasks to retrieve per page (default: 10).

**Response**

- Status Code: 200 (OK)
- Body:
```json
{
    "data": [
        {
            "id": 1,
            "title": "Task 1",
            "description": "Description of Task 1",
            "due_date": "01/01/2023",
            "status": "Completed"
        },
        ...
    ],
    "total_pages": 5
}
```

### Get Task by ID

Retrieves a specific task by its ID.

**Endpoint**: `/task/{task_id}`

**Method**: GET

**Parameters**:

- `task_id`: The ID of the task to retrieve.

**Response**

- Status Code: 200 (OK)
- Body:
```json
{
    "id": 1,
    "title": "Task 1",
    "description": "Description of Task 1",
    "due_date": "01/01/2023",
    "status": "Completed"
}
```

### Create Task

Creates a new task.

**Endpoint**: `/task/create`

**Method**: POST

**Request Body**:

- `title` (required): The title of the task.
- `description` (required): The description of the task.
- `due_date` (required): The due date of the task in the format "DD/MM/YYYY".
- `status` (required): The status of the task (options: "Incomplete", "In Progress", "Completed").

**Response**

- Status Code: 200 (OK)
- Body:
```json
{
    "message": "Adding a task was successful!"
}
```

### Update Task

Updates an existing task.

**Endpoint**: `/task/update`

**Method**: PUT

**Request Body**:

- `id` (required): The ID of the task to update.
- `title` (optional): The updated title of

 the task.
- `description` (optional): The updated description of the task.
- `due_date` (optional): The updated due date of the task in the format "YYYY-MM-DD".
- `status` (optional): The updated status of the task (options: "Incomplete", "In Progress", "Completed").

**Response**

- Status Code: 200 (OK)
- Body:
```json
{
    "message": "Updated the task"
}
```

### Delete Task

Deletes a specific task by its ID.

**Endpoint**: `/task/delete/{task_id}`

**Method**: DELETE

**Parameters**:

- `task_id`: The ID of the task to delete.

**Response**

- Status Code: 200 (OK)
- Body:
```json
{
    "message": "Task has been deleted successfully"
}
```
