class Person:
    x = 5
    name = "Thierry"

    def __init__(self, name, age ):
        self.name = name
        self.age = age
    
    def greet(self):
        return "Hello, my name is " + self.name
    
    @staticmethod
    def className():
        return "I am an static method of the class"



p1 = Person("Thierry", 23)
print(p1.name)
print(p1.age)
print(p1.greet())

p2 = Person("Jado", 20)
print(p2.name)
print(p2.age)
print(p2.greet())

print(Person.className())
print(Person.x)


# class Student(Person):
#     pass

# stud1 = Student("Kamali", 34)
# print(stud1.name)
# print(stud1.age)
# print(stud1.greet())

# print(Student.className())


class Student(Person):
    def __init__(self, name, age, species):
         super().__init__(name, age)
         self.species = species
    
    def greet(self):
        parentGreet = super().greet()
        return parentGreet + " ---> Hello, Call me " + self.name + " and I am from " + self.species + " species"
    
    @staticmethod
    def className():
        return Person.className()

stud1 = Student("Kamali", 34, "dog")
print(stud1.name)
print(stud1.age)
print(stud1.greet())

print(Student.className())



#dependancy injection

# with static method and class-level variable
class A():
    number = 3
    @staticmethod
    def findNumber():
        return A.number


print("......")
class B():
    def __init__(self, instance_of_A, multiplier):
        self.instance_of_A = instance_of_A
        self.multiplier = multiplier
    
    def result(self):
        return self.instance_of_A * self.multiplier
    

inst_A = A.findNumber()
inst_B = B(inst_A, 2)
print(inst_B.result())


#dependancy injection

# with instance method and class-level variable
class A():
    number = 3

    def findNumber(self):
        return A.number  # always an instance method is characterized by self keyword and we can access a class-level variable with self. because it will stat find the variable inside the constructor if it doesn't find it it will use the class-level variable or we can even accessit without self. buy just className.variable A.number


print("......")
class B():
    def __init__(self, instance_of_A, multiplier):
        self.instance_of_A = instance_of_A
        self.multiplier = multiplier
    
    def result(self):
        return self.instance_of_A * self.multiplier
    

inst_A = A().findNumber()  #will be access as instance method
inst_B = B(inst_A, 2)
print(inst_B.result())




#Getters and Setters in Python

class Villa:
    def __init__(self, name):
        self._name = name

    @property
    def name (self):
        return self._name
    

    @name.setter
    def name (self, value):
        self._name = value
    

v1 = Villa("The Gym")
print(v1.name)

v1.name = "The Palace"
print(v1.name)



# class Method

class Counter:
    count = 0

    def __init__(self, name):
        self.name = name
        Counter.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count


c1 = Counter("First Count")
print(c1.get_count())
c2 = Counter("Second Count")
print(c2.get_count())






    








