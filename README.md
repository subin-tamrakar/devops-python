# Python Calculator - DevOps Lab

This project contains a simple Python calculator API built with **FastAPI**. It is designed to be used as a hands-on lab for learning **Jenkins Declarative Pipelines**.

## Project Overview

 The application is a simple REST API that provides basic arithmetic operations:
- **Add**: `/add?a=1&b=2`
- **Subtract**: `/sub?a=10&b=4`
- **Multiply**: `/mul?a=3&b=3`
- **Divide**: `/div?a=10&b=2`

## Local Development Instructions

Follow these steps to run the application locally on your machine.

### Prerequisites
- Python 3.10+
- `pip`

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
Start the server using `uvicorn`:
```bash
uvicorn app:app --reload
```
The API will be available at `http://127.0.0.1:8000`. You can access the interactive documentation at `http://127.0.0.1:8000/docs`.

### 3. Run Tests
Execute the unit tests using `pytest`:
```bash
pytest
```

---

## Lab Assignment: Jenkins Declarative Pipeline

Your goal is to automate the lifecycle of this application using Jenkins. You will create a `Jenkinsfile` that defines the pipeline.

**Note**: A reference solution is provided in the `Jenkinsfile` (if available), but try to implement it yourself first!

### Assignment 1: Pipeline Initialization & Versioning
**Goal**: Create a basic `Jenkinsfile` and determine the application version.
- Define a declarative pipeline.
- Set the agent to `any`.
- **Challenge**: In an `Init` stage, add a script to extract the version from the latest `git tag`. If no tag is found, fallback to the `BUILD_NUMBER`.

### Assignment 2: The Build Stage
**Goal**: Ensure the application dependencies can be installed.
- Create a `Build` stage.
- Add steps to install the Python dependencies listed in `requirements.txt`.

### Assignment 3: The Test Stage
**Goal**: Verify the application logic.
- Create a `Test` stage.
- Run the unit tests using `pytest`.
- **Bonus**: Configure the pipeline to archive the test results (e.g., using JUnit or `pytest --junitxml`).

### Assignment 4: The Deploy Stage
**Goal**: Simulate a deployment to a server.
- Create a `Deploy` stage.
- Since we don't have a live production server for this lab, print the shell commands you *would* run to deploy the app.
- **Requirements**:
    - Print the command to restart the `systemd` service (`calculator.service`).
    - Print the command to reload the `nginx` configuration (`nginx.conf`).
    - Mention the version number being deployed in the logs.

## Deployment Files
- `nginx.conf`: Nginx configuration for reverse proxying the app.
- `calculator.service`: Systemd unit file for managing the application process.
