# Flask Task Manager Backend

This is a simple backend application built using Flask and MongoDB. It serves as the backend for a task management system, exposing API endpoints and rendering tasks through a web interface.

## Features

* RESTful API for task CRUD operations
* Server-side rendering of tasks via Jinja2 templates
* MongoDB integration for persistent storage
* CORS support for communication with a frontend application

## Technology Stack

* Python 3.13
* Flask
* MongoDB (via PyMongo)
* Jinja2 for HTML templating
* CORS via Flask-CORS

## Project Structure

```
backend-flask-app/
├── main.py
├── core/
│   ├── config.py
│   ├── models.py
│   └── routes.py
├── templates/
│   └── index.html
└── requirements.txt
```

## Getting Started

### Prerequisites

* Python 3.13+
* MongoDB instance (local or cloud)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yasserfedsi/backend-flask-app.git
cd backend-flask-app
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# On macOS
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure MongoDB settings in `.env` file:

```python
MONGO_URI = "your-mongodb-uri"
DB_NAME = "your-db-name"
COLLECTION_NAME = "your-collection-name"
```

### Running the App

```bash
python main.py
# Or
py main.py
```

Visit `http://127.0.0.1:5000` to view the rendered task list.

## Deployment

This backend can be deployed to any platform that supports Flask, such as:

* Vercel (via Python Serverless Function)
* Render
* Heroku

When deploying to Vercel:

* Ensure your `app.py` is compatible with serverless deployment.
* Use a `vercel.json` and include necessary build configurations.

## License

This project is licensed under the <a href="https://github.com/yasserfedsi/backend-flask-app/blob/main/LICENSE" style="text-decoration: none; color: inherit;" target="_blank">MIT</a> License.
