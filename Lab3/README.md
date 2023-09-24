# Lab 3

<img align="right" src="./media/patterns.png" width="400px"/>


> "Design Patterns"

Whether you start working in industry, your own startup, or as a researcher, there is a strong likelihood that the projects you are going to develop or work on are going to grow in size. It's not uncommon to be working on codebases of millions of lines each release of the project. Because our brains can only hold so much information, we often need to rely on useful abstractions to help us organize and maintain all of the information. Today we are going to practice refactoring our code, and then implementing a design pattern.

For your lab today, you will learn object-oriented programming and a design pattern.

# Implementation Logistics

- You may use whatever operating system, IDE, or tools for completing this assignment.
	- However, my instructions will usually be using the command-line, and that is what I will most easily be able to assist you with.
- In the future there may be restrictions, so please review the logistics each time.

# Resources to help

Provided below are a list of curated resources to help you complete the tasks below. Consult them (read them, or do Ctrl+f for keywords) if you get stuck.

- Task 1
	1. https://realpython.com/inheritance-composition-python/
		- Disucssion on composition vs inheritance.
- Task 2
	1. Singleton Pattern deep dive
		- [Design Patterns - Singleton Pattern](https://python-patterns.guide/gang-of-four/singleton/)
	
# Task 1 - Inhertiance vs Composition

## Object-Oriented Programming

<img align="right" width="400px" src="./media/inheritance.jpg">

We want to get in the habit of writing code that is modular and maintainable. Often that means reducing [coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) in our code such that our codebase can be changed without efforts to rearchitect the entire product. One common way developers create new types however, is by the use of inheritance. A reminder that inheritance is the ability to create a new sub-class (the new thing we are creating) by deriving from a pre-existing base class. One problem with this however, is that sometimes the inheritance hierarchy can quickly grow out of control, and our code becomes very 'coupled' together.

### Your task

Take a moment to look at the code labeled [./src/oop.py](./src/oop.py). 

**You task** Review [./src/oop.py](./src/oop.py) and respond to questions by [exercises.md](./exercises.md).

# Task 2 - Design Pattern

## Singleton

The Singleton pattern is a design pattern that we have previously learned about. Some say having one object that is globally scoped is never worth having and take a strong stance towards never having global objects (i.e. The singleton pattern is an anti-pattern). However, sometimes the singleton can be useful if we need a single place to log information (Note: With threads we may need to think more about our design and have locks for instance). 


Refactor the logger provided in [./src/singleton.py](./src/singleton.py) with the following changes requested in [exercises.md](./exercises.md).

## Testing

- Make sure your code for Task 1 and Task 2 compiles.

# Submission/Deliverables

- Task 1
	- Make sure you answered your questions in [exercises.md](./exercises.md).
- Task 2
	- We are going to review your refactored [./src/singleton.py](./src/singleton.py) to see an implementation of a logger.
	- Then look to make sure you answered your questions in [exercises.md](./exercises.md).

### Submission

- Commit all of your files to github, including any additional files you create.
- Do not commit any binary files unless told to do so.
- Do not commit any 'data' files generated when executing a binary.

# Rubric

You (and any partner(s)) will receive the same grade from a scale of 0-2. Both partners should commit the same code.

- 0 for no work completed by the deadline
- 1 for some work completed, but something is not working properly
- 2 for a completed lab (with possible 'going further' options completed)

# Going Further

An optional task(if any) that will reinforce your learning throughout the semester--this is not graded.

1. Try implementing more design patterns that you have learned today!

