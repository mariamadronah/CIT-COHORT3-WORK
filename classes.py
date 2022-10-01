#create a credit card class with the following attributes: 
# card number, expiration date, and security code. 
# Create a method that will print out the card number, expiration date, and security code.
# Create an instance of the class and call the method.

class credit_card:
    def __init__(self, card_number, expiration_date, security_code ):
        self.card_number= card_number
        self.expiration_date= expiration_date
        self.security_code= security_code
    def __repr__(self):
        return (f"card number is: {self.card_number}\nExpiration date is :{self.expiration_date}\nSecurity code is : {self.security_code} ")
friend= credit_card(23456789, 2024, 1234)
print(friend)

print("==================================================================================")

#create Animal class and Dog class. Make the Dog class inherit from the Animal class. 
# Add a bark method to the Dog class.
#  Create an instance of the Dog class and call the bark method.

class Animal:
    def __init__(self, color, breed):
        self.color = color
        self.breed=breed

class Dog(Animal):
    def bark(self):
        print("bark!")

grey= Dog('black', 'german')
grey.bark()
print("==================================================================================")
#3. create a class called Queue. The class should have the following methods: 
# enqueue, dequeue, and size. The enqueue method should add an item to the queue. 
# The dequeue method should remove an item from the queue. The size method should return the size of the queue.

class Queue:
    def __init__(self):
        self.queue = list()

    

    # add an element to the queue
    def enqueue(self, data):
        # insert method to add element
        self.queue.insert(0, data)
        return True

    # remove an element from the queue
    def dequeue(self):
        return self.queue.pop()

    # size of the queue
    def size(self):
        return len(self.queue)

    # display the queue
    def display(self):
        return self.queue


line = Queue()

# insert elements to the queue
line.enqueue(4)
line.enqueue('dog')
line.enqueue(True)

# display the queue
print(line.display())

# remove an element from the queue
print(line.dequeue())

# display the queue
print(line.display())
# check the size of the queue
print(line.size())


print("==================================================================================")
#4.create a class called Stack. The class should have the following methods: push, pop, and size. 
# The push method should add an item to the stack. 
# The pop method should remove an item from the stack. The size method should return the size of the stack.
class Stack:
    def __init__(self):
        self.stack = list()

    
    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.isEmpty():
            return ("Stack is empty. Stack Underflow :(")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

tin = Stack()

tin.push('pencil')
tin.push('pen')
tin.push('ruler')
print(tin.show())
print(tin.pop())
print(tin.show())
print(tin.size())

print("==================================================================================")
#5.create a class called Person. The class should have the following attributes: name, age, and address. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working".


class Person:
    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.address=address

    def eat(self):       
        return(f"{self.name} is eating")

    def sleep(self):
        return (f"{self.name} is sleeping")

    def work(self):
        return (f"{self.name} is working")

mariam = Person('mary', 12, 'jinja')
print(f"My name is {mariam.name}, aged {mariam.age} and I stay in {mariam.address}")
print(mariam.eat())
print(mariam.sleep())
print(mariam.work())
        
print("===================================================")       
#6.create a class called Employee. The class should have the following attributes: name, age, and salary. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working". 
# Create a subclass of Employee called Programmer. 
# The Programmer class should have the following attributes: name, age, salary, and programming language. 
# The Programmer class should have the following methods: eat, sleep, work, and code. 
# The code method should print out the name of the person and the word "is coding in" and the programming language.
#  Create an instance of the Programmer class and call all the methods.
class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary

    def eat(self):       
        return(f"{self.name} is eating")

    def sleep(self):
        return (f"{self.name} is sleeping")

    def work(self):
        return (f"{self.name} is working")

class Programmer(Employee):
    def __init__(self,name, age, salary,programming_language):
        super().__init__(name, age, salary)
        self.programming_language= programming_language

    def code(self):
        return (f"{self.name} is coding in {self.programming_language}")



mariam = Employee('mary', 12, 'jinja')
me= Programmer('mary', 12, 'jinja','python')
print(mariam.eat())
print(mariam.sleep())
print(mariam.work())
print(me.code())

print("==================================================================================")
#7. create a class called Vehicle. The class should have the following attributes: make, model, and year. 
# The class should have the following methods: start, stop, and drive. 
# The start method should print out the make, model, and year of the vehicle and the word "is starting". 
# The stop method should print out the make, model, and year of the vehicle and the word "is stopping". 
# The drive method should print out the make, model, and year of the vehicle and the word "is driving". 
# Create a subclass of Vehicle called Car. The Car class should have the following attributes: make, model, year, and color. 
# The Car class should have the following methods: start, stop, drive, and park. 
# The park method should print out the make, model, year, and color of the car and the word "is parking". 
# Create an instance of the Car class and call all the methods.

class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary

    def eat(self):       
        return(f"{self.name} is eating")

    def sleep(self):
        return (f"{self.name} is sleeping")

    def work(self):
        return (f"{self.name} is working")

class Programmer(Employee):
    def __init__(self,name, age, salary,programming_language):
        super().__init__(name, age, salary)
        self.programming_language= programming_language

    def code(self):
        return (f"{self.name} is coding in {self.programming_language}")

print("==================================================================================")
#8. create a class called Animal. The class should have the following attributes: name, color, and age. 
# The class should have the following methods: eat, sleep, and make_sound. 
# The eat method should print out the name of the animal and the word "is eating". 
# The sleep method should print out the name of the animal and the word "is sleeping".
# The make_sound method should print out the name of the animal and the word "is making a sound". 
# Create a subclass of Animal called Dog. The Dog class should have the following attributes: name, color, age, and breed. 
# The Dog class should have the following methods: eat, sleep, make_sound, and bark. 
# The bark method should print out the name of the dog and the word "is barking". 
# Create an instance of the Dog class and call all the methods.

class Animal:
    def __init__(self,name, color,age):
        self.name=name
        self.color=color
        self.age= age

    def eat(self):       
        return(f"{self.name} is eating")

    def sleep(self):
        return (f"{self.name} is sleeping")

    def make_sound(self):
        return (f"{self.name} is working")

class Dog(Animal):
    def __init__(self,name, color,age,breed):
        super().__init__(name, color,age)
        self.breed=breed

    def bark(self):
        return (f"{self.name} is barking")

Dog1= Dog("John", "brown", 5, "german" )
print(Dog1.eat())
print(Dog1.sleep())
print(Dog1.make_sound())
print(Dog1.bark())

print("==================================================================================")   

#9. create a class of your choice. 
# It should have at least 3 attributes and 3 methods where one of the methods is a static method. 
# Implement polymorphism, encapsulation, and inheritance.

class Student:
    def __init__(self,name,age, combination):
        self.name=name
        self.__age= age
        self.combination=combination

    def study(self):       
        return(f"{self.name} is studying")

    def sleep(self):
        return (f"{self.name} is sleeping")

    def read(self):
        return (f"{self.name} is reading")


    
class pupil(Student):
    def __init__(self,name, age,combination):
        super().__init__(name,age, combination)
        

    

student1= pupil("John", 5,"PEM" )
print(student1.name)
print(student1.combination)
print(student1.age)



