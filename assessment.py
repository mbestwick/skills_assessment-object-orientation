"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   (1) Encapsulation - a design advantage because when data (attributes) lives
   close to its functionality (methods), you can use your data to its best
   potential. Having all your tools in one place allows you to keep track of
   your possibilities and maximize your functionality.

   (2) Abstraction - saves the user (programmer) from knowing/executing the
   details of a method/function and frees them up to focus on the bigger problems
   at hand. As long as they know what will come out when they put something into
   a "black-box", they can use it quickly and efficiently.

   (3) Polymorphism - the programmer can make interchangeable types of classes,
   which gives them an incredible amount of flexibility and the power to make
   specific tools for specific jobs. When they can form their own unique tools
   to perform a task, it provides them infinite ways to solve a single problem!!

2. What is a class?

    To put it simply, a type of "thing" - an object that you can use - in Python.

3. What is an instance attribute?

    An attribute that is explicitly assigned to a single instance of a class.
    It is not shared with other instances of the same class, unless specifically
    assigned to another instance.

4. What is a method?

    A function defined within a class that can be performed on any instance of
    that class.

5. What is an instance in object orientation?

    A single occurence of a defined class. If iPhones were a class, my specific
    iPhone that I use every day would be an instance of the iPhone class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is defined in the class definition. When an instance of
   a class occurs, that instance immediately holds each of those attributes.
   However, if you explicitly assign an instance its own particular attribute,
   then it has an instance attribute that is unique from other instances of the
   class.
   For example, if we have a Student class

            class Student(object):
                profession = "student"
                job = "to learn"

    then ever instance of Student has the class attributes of profession and job,
    and the value is the same for each.

    But say, one of your instances (joe) decides to get a job in the cafeteria.
    You would do the following:

            joe.job = "serve food"

    The instance joe now has a unique instance attribute of job = "serve food",
    and that attribute supercedes the class attribute of job. When searching for
    a value of an instance attribute, Python first searches in the instance
    attributes, and if not there, then moves to search in the class attributes.


"""


# Parts 2 through 5:
# Create your classes and class methods
