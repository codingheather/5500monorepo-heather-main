# Implementation Logistics

# Resources to help

* https://www.uvicorn.org/
* https://fastapi.tiangolo.com/
* https://curl.se/docs/httpscripting.html
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST

# Task 0

* Create a virtual environment
* Install fastapi, uvicorn, pytest, pytest-cov
* Create a GET ReST API
* Create a GET ReST API with path parameters
* Create a GET ReST API with query parameters
* Create a GET ReST API with path parameters AND query parameters
* Create a POST ReST API
* Create a PUT ReST API 
* Create a DELETE ReST API

Run your web server using the following:
`uvicorn <path to module with fastapi app>:<name of app> --reload`

Test your API's using `curl`. For example, to test a GET ReST API deployed locally:

`curl 'http://localhost:8000/books/?category=fiction'`


# Task 1

* Create a folder called "tests"
* Write some tests and put them in the tests folder; you do not have to cover every function that you have written
* Run pytest to see the code coverage based on your tests. For example:
`pytest --cov=src tests/`

  

# Submission/Deliverables

### Submission
- Commit all of your files to GitHub, including any additional files you create.

### Deliverables

- Task 0, 1
  - In the [todo_app](./todo_app) folder, add all your files created during in Task 0 and 1. DO NOT commit your virtual environment folder. 

# Rubric

You (and any partner(s)) will receive the same grade from a scale of 0-2. Both partners should commit the same code.

- 0 for no work completed by the deadline
- 1 for some work completed, but something is not working properly
- 2 for a completed lab (with possible 'going further' options completed)
