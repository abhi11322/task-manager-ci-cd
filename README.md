# Task Manager CI/CD

A simple Flask REST API built to learn and demonstrate the fundamentals of **CI/CD, GitHub Actions, Docker, GitHub Container Registry (GHCR), and automated deployment**.

## Tech Stack

- Python 3.12
- Flask
- Pytest
- Docker
- GitHub Actions
- GitHub Container Registry (GHCR)
- Render

## Features

The API supports basic task management:

- Create a task
- Get all tasks
- Complete a task
- Delete a task
- Validate that a task has a title

## API Endpoints

### Get all tasks

```http
GET /tasks
```

### Create a task

```http
POST /tasks
Content-Type: application/json

{
  "title": "Learn CI/CD",
  "description": "Build a basic CI/CD pipeline"
}
```

### Complete a task

```http
PUT /tasks/<task_id>/complete
```

### Delete a task

```http
DELETE /tasks/<task_id>
```

## Run Locally

Clone the repository and create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## Run Tests

Run the test suite with:

```bash
pytest
```

The same tests are automatically executed by GitHub Actions.

## Docker

Build the Docker image:

```bash
docker build -t task-manager .
```

Run the container:

```bash
docker run -p 5000:5000 task-manager
```

The application will then be available at:

```text
http://localhost:5000/tasks
```

## CI/CD Pipeline

This project uses GitHub Actions to automate testing and deployment.

### Pull Request

When a Pull Request targets `main`, GitHub Actions:

1. Checks out the code
2. Sets up Python 3.12
3. Installs dependencies
4. Runs the Pytest test suite
5. Builds the Docker image

This prevents code that fails the automated checks from being merged.

### Main Branch

When changes are pushed to `main`, the pipeline:

1. Runs the tests
2. Logs into GitHub Container Registry
3. Builds the Docker image
4. Pushes the Docker image to GHCR
5. Triggers the Render deployment using a deployment hook

### Pipeline Overview

```text
Developer
    |
    v
Feature Branch
    |
    v
Pull Request
    |
    v
GitHub Actions
    |
    +--> Run Tests
    |
    +--> Build Docker Image
    |
    v
Merge to main
    |
    +--> Run Tests
    |
    +--> Build Docker Image
    |
    +--> Push Image to GHCR
    |
    +--> Trigger Render Deployment
    |
    v
Live Application
```

## Git Workflow Used

The project follows a basic feature-branch workflow:

```text
main
 |
 +---- feature/add-task-validation
             |
             +---- Code changes
             +---- Tests
             +---- Push branch
             +---- Pull Request
             +---- CI checks
             |
             +---- Merge into main
```

Example:

```bash
git checkout -b feature/my-change

# Make changes

git add .
git commit -m "Add my change"
git push -u origin feature/my-change
```

Then create a Pull Request targeting `main`.

After the CI checks pass, merge the Pull Request.

## Project Structure

```text
task-manager-ci-cd/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## What This Project Demonstrates

This project was created as a practical introduction to:

- Continuous Integration (CI)
- Continuous Deployment (CD)
- Automated testing
- Git branching
- Pull Requests
- GitHub Actions
- Docker containerization
- Container image registries
- Automated deployment
- Basic deployment pipelines

## Learning Outcome

The goal of this project is not to build a production-grade task manager. It is a small application used to understand how code moves from:

```text
Local Development
        ↓
Git
        ↓
Pull Request
        ↓
Automated Tests
        ↓
Docker
        ↓
Container Registry
        ↓
Deployment
        ↓
Live Application
```

This provides a foundation for learning more advanced DevOps and CI/CD concepts later.
