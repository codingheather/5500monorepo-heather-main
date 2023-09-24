# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- It is a concrete class. The class is not derived from ABC and can be instantiated. 
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- It is a destructor method. It is called when an object is garbage collected which happens at some point after all references to the object have been deleted.
1. What class does Texture inherit from?
	- Image class
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- It gets all the public base class member functions (getWidth, getHeight, getPixelColorR, getPixels, setPixelsToRandomValue) and attributes (m_width, m_height, m_colorChannels, m_Pixels)
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- "has-a" (composition) relationship. An image is usually part of a texture instead of a specific kind of image as texture has other features as well. For example, the texture of my carpet includes an image as well as material.
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Python will automatically generate the default constructor for the child class based on the super class's constructor. When class Texture does not declare a constructor then python looks up it's base class Image. Since Image has its constructor declared, class Texture will inherit the super class's constructor.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?
	-  No. When it is first used - when the singleton's static variable is null - two or more threads attempting to use it would read its static variable as null and would make the singleton create a new instance more than once, leading to memory leak.
	- need to add a lock like "__singleton_lock = threading.Lock()" for a thread safer implementation. 
  
