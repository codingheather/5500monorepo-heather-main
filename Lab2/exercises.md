# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

No. For example, in dictionary, list(d) returns a list of all the keys used in the dictionary d. So it should be 'listKey' to be correlated to what it does. Another example in list would be append(x). This member function is used to append x to the end of the sequence. A better version would be 'endAppend'


2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

Dictionary is a mapping object. It is implemented with hastables.
However, list is a sequence, and it is implemented with arrays.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, it allow for random access by index. 

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Pros:
 - save memory. Do not need to create multiple list/set/dictionary/etc for different data types. 

Cons:
 - easily messed up. If a list has elements with various data types, it might be hard to keep track each element's type and write bug-free code. 

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

No. For example, requests.request(method, url, **kwargs) suppose to construct and send a Request. A better name would be 'constructAndSendRequest' to better describe the action the code is doing. 

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

I do not see any member function that include lots of arguments more than 5. The most I have seen is 'iter_lines', which contains 3 arguments in the lower-level classes section. 

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

**kwargs allows caller to pass keyworded variable length of arguments to a function. 
Good:
 - allows caller to pass any number of keyword arguments
Bad:
 - hard to debug as python will not tell the engineer the parameter is missing

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

'None' is considered as the default value for the arguments that are set to 'None'. For example, for the method patch(self, url, data=None, **kwargs), when there is no 'data' value passed in, 'None will be used during executation.
Yes, the arguments can be set to anything besides 'None' as long as it is reasonable to the specific program. 
Assigning a default value into a keyword argument can make sure that the function can still work even if there is no value passing to the keyword argument.
