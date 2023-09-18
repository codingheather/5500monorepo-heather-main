# Assignment - Extending the json standard library 

<img align="right" width="300px" src="./media/dart.jpg">

> "Finding your domain"

*You've decided to take the plunge as a Python programmer.*

*And picking a domain of where you want to specialize is the next question. And this is something you have pondered quite a bit, trying to figure out where you want to apply your efforts. Sometimes finding your niche requires just trying a few different things.*

*All of a sudden you find a blog post about extending the json standard library.  How cool you think--hmm, where can I get started?*


# Resources to help

Provided below are a list of curated resources to help you complete the task(s) below. Consult them (read them, or do ctrl+f for keywords) if you get stuck.

https://docs.python.org/3/library/json.html

https://docs.python-guide.org/scenarios/serialization/

https://realpython.com/python-wheels/

https://mathspp.com/blog/custom-json-encoder-and-decoder


# Your Task

## Task 0 - Learning a new standard library

Learning a new API can be a bit overwhelming. In my experience when you start off a new job, you are often thrown into a large codebase with  little documentation. One skill you should learn is that it is okay to ask for help from your colleagues when this happens. However, if this is not an option, you'll have to have a few techniques to learn more about the codebase. Here are my tips and advice:

1. If it's a public API (i.e. not internal to the company), search for tutorials!
2. If it is internal, find out if there is documentation.
3. Learn where to look in the source code for help.
4. Search to see if there are examples included in the source, or even unit tests that may help uncover basic functionality of the API.

Your first task is going to be to get acquainted with Python's json standard library, setuptools, and some blogs on how to extend the json library.

### Task 1 - Extend the json standard library

Look at the examples seen in https://docs.python.org/3/library/json.html and https://mathspp.com/blog/custom-json-encoder-and-decoder. 

Your extended library should consist of one module, `jsonapi.py`. That module should have the following:
* A subclass of json.JSONEncoder
* A subclass of json.JSONDecoder
* A function named `dumps` that serves as a wrapper around the `json.dumps` function
* A function named `loads` that serves as a wrapper around the `json.loads` function

### Task 2 - Write some tests

You should write tests for each of the classes and functions defined in your `jsonapi.py` module. Those tests should use complex and range objects as objects to be serialized and deserialized.


# Submission/Deliverables

### Submission

- Commit all of your files to github, including any additional files you create.
- Do not commit any binary files unless told to do so.
- Do not commit any 'data' files generated when executing a binary.

### Deliverables

- Task 3
	- A working [./../part1/jsonapi.py](./../part1/jsonapi.py) in the [../part1](../part1) directory.
    - A working [./../part1/test_jsonapi.py](./../part1/test_jsonapi.py) in the [../part1](../part1) directory.

# Going Further

An optional task(if any) that will reinforce your learning throughout the semester--this is not graded.

1. Feel free to play more with the json standard library. What are some other serialization tools that Python provides? Look into `pickle` and `marshal`.
