# Lab 2

<img src="./media/logo.png" align="right" width="500px"/>

> "Looking at APIs"

An important part of building software is to build an Application Programming Interface (API) that can support you. 
The more reusable, scalable, and maintainable the API is the better. Well-designed APIs can also be shared amongst 
your team members through multiple projects speeding up development time. Planning a good API up front can be an 
important part of the planning stage of the software development life cycle(SDLC) as well.

For your lab today, you will be getting acquainted with Python and git again. You will additionally be looking at 
some APIs and programming libraries so you can get an idea of what a good API is when designing your own.

# Implementation Logistics

- You may use whatever operating system, IDE, or tools for completing this assignment.
	- However, my instructions will usually be using the command-line, and that is what I will most easily be able to assist you with.
- In the future there may be restrictions, so please review the logistics each time.

# Resources to help

Provided below are a list of curated resources to help you complete the tasks below. Consult them (read them, or do Ctrl+f for keywords) if you get stuck.

- Task 1
	1. [Pro Git book](https://git-scm.com/book/en/v2/)
		* The first three chapters freely available will help you if you are struggling with Task 1.
	2. [Sample gitignores](https://github.com/github/gitignore)
		* See a comprehensive list of .gitignore files
		* See additional notes on gitignore here: https://git-scm.com/docs/gitignore
	3. [Git Beginner Masterclass](https://www.youtube.com/watch?v=HlYJpuwaXiE&list=PLvv0ScY6vfd-GGT-aUH31X2yXgBSYXo6t&index=5)
		* My crash course introduction to Git
- Task 2
	1. [Python Standard Library](https://docs.python.org/3/library/index.html)
		* See built-in functionality in the langauge.

# Task 1 - More Git (Reading + 1 action item)

Please complete the reading and update the `.gitignore` file in this repo. See Deliverables, Task 1

# Task 2 - Basic Python APIs (Reading + 1 action item)

For this task you are going to be analyzing the Python [Standard Library](https://docs.python.org/3/library/index.html) 
(SL) and another API called [requests](https://requests.readthedocs.io/en/latest/).

The SL is a good example of an application programming interface where much thought has been given to the design and 
for the clients who will be using the SL (such as us Python developers). It may not be 100% perfect, 
but it is a good starting point to look at Application Programming Interfaces (APIs).

[requests](https://requests.readthedocs.io/en/latest/) is a third-party library that has been around for quite some time
and is considered a good example of intuitive API design. 

## Prompt

### Python Standard Library

When learning a new programming language, often times that involves learning the key libraries associated with it so 
that we do not have to rebuild everything from scratch. Reinventing and relearning data structures in a new language is a good practice, 
but for us that will not be necessary as we can take advantage of the standard library provided by Python. Because the 
standard library is widely distributed, much thought is taken to make it execute in a uniform way and predictable way. 
A good API will also abstract out a lot of the implementation details, so you only need to worry about what you need 
to do (Note: Knowing what is going on behind the scenes is important for security and performance however).

### requests

While Python does provide the standard libraries `http` and `urllib` for making http requests, `requests` extends those 
libraries by providing more features and creating a more user-friendly interface.

## Your Task (Your action item)

Modify the [exercises.md](./exercises.md) after visiting each of the pages below:

1. [mapping types](https://docs.python.org/3/library/stdtypes.html#typesmapping)
2. [sequence types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
3. [requests](https://requests.readthedocs.io/en/latest/)
 
## Testing

We will be looking at your repository to see that you have a .gitignore file in your repository, and that you have answered the questions in [exercises.md](./exercises.md).

# Submission/Deliverables

### Submission

- Commit all of your files to github, including any additional files you create.
- Do not commit any binary files unless told to do so.
- Do not commit any 'data' files generated when executing a binary.

### Deliverables

- Task 1
	- add/commit/push a [.gitignore](./.gitignore) file to the root directory of your monorepo on the main branch.
- Task 2
	- Modify the [exercises.md](./exercises.md) 
	- add/commit/push your [exercises.md](./exercises.md) 

# Rubric

You (and any partner(s)) will receive the same grade from a scale of 0-2. Both partners should commit the same code.

- 0 for no work completed by the deadline
- 1 for some work completed, but something is not working properly
- 2 for a completed lab (with possible 'going further' options completed)

# Going Further

An optional task(if any) that will reinforce your learning throughout the semester--this is not graded.

1. Investigate other data structures provided in Python Standard Library (i.e. map, queue, ordered dictionary).

# F.A.Q. (Instructor Anticipated Questions)

1. Q: Should I always be working in another branch?
	- A: Yes, it's a good habit to start forming now.
