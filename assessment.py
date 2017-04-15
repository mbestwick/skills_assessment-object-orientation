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
   a class occurs, that instance immediately holds each of the class attributes.
   However, if you explicitly assign an instance its own particular attribute,
   then it has an instance attribute that is unique from other instances of the
   class.
   For example, if we have a Student class

            class Student(object):
                profession = "student"
                job = "to learn"

    then every instance of Student has the class attributes profession and job,
    and the value is the same for each.

    But, say one of your instances (joe) decides to get a job in the cafeteria.
    You would do the following:

            joe.job = "serve food"

    The instance joe now has a unique instance attribute of job = "serve food",
    and that attribute supercedes the class attribute job. When searching for
    a value of an instance attribute, Python first searches in the instance
    attributes, and if not there, then moves to search in the class attributes.

    You would assign an instance attribute if there is something unique about that
    instance that you want to be reflected in your code (because it will be used
    over the class attribute). On the other hand, if you want the instance to have
    the same attributes as the rest of its class, you would defer to the class
    attribute and not assign an instance attribute.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """ A student. """

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        # example in the instructions shows a single dictionary of all attributes
        self.data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address
            }

    def __repr__(self):
        return "A student with a first name, last name, and address."


class Question(object):
    """ A question and answer. """

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.data = {
            'question': self.question,
            'correct_answer': self.correct_answer
            }

    def __repr__(self):
        return "A question and a correct answer."


class Exam(object):
    """ An exam. """

    def __init__(self, name):
        self.questions = []
        self.name = name
        self.data = {
            'name': self.name,
            'questions': self.questions
            }

    def __repr__(self):
        return "List of dictionaries, each w/ an exam question & correct answer."

    def add_question(self, question):
        self.questions.append({ "question": question.question,
                                "correct_answer": question.correct_answer})

    def ask_and_evaluate(self, i=-1):    # defaults to last question added
        question = self.questions[i]['question']
        correct_answer = self.questions[i]['correct_answer']
        user_answer = raw_input("{} > ".format(question))
        if user_answer == correct_answer:
            return True
        else:
            return False

    def administer(self):
        questions_asked = 0
        questions_correct = 0

        for i in range(len(self.questions)):
            questions_asked += 1
            if self.ask_and_evaluate(i) is True:
                questions_correct += 1

        score = 100 * float(questions_correct) / questions_asked
        print score


class Quiz(Exam):
    """ A quiz. """

    def __repr__(self):
        return "List of dictionaries, each w/ a quiz question & correct answer."


class StudentExam(object):
    """ An exam taken by a student. """

    def __init__(self, student, exam):
        self.name = student.first_name
        self.exam = exam
        self.score = None

    def __repr__(self):
        return "A student's name, an exam they took, and their score on the exam"

    def take_test(self):
        self.exam.administer()


def example():
    """ Creates an exam and a student, then administers the exam to the student. """

    student = Student('Michela', 'Bestwick', '235 Mallorca Way')

    q1 = Question("What is the capitol of California?", "Sacramento")
    q2 = Question("Who won the 1989 World Series?", "Oakland A's")
    q3 = Question("What was Ronald Reagan's favorite candy?", "jelly beans")

    midterm = Exam('midterm')

    midterm.add_question(q1)
    midterm.add_question(q2)
    midterm.add_question(q3)

    student_exam = StudentExam(student, midterm)

    student_exam.take_test()


example()


















