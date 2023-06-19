#Md Hussain
#Day 9


#class

class Student: #Defined class named 'Studnet'
    university = "University at Buffalo" #class variable
    
    def __init__(self, name, age, major): #constructor/initializer
        self.name = name #value of instance variable self.name[which you will use later]
        #is the same as 'name'
        self.age = age
        self.major = major

    def study(self):
        print(f"{self.name} is studying.")

    def swim(self):
        print(f"{self.name} is swimming.")

    def major_and_age(self):
        print(f"{self.name} studies {self.major} in {Student.university} and is {self.age}"
              " years old.")
        
student1 = Student("Ishmam", 20, "Computer Science") #This is a student object stored as student1
student2 = Student("Sameer", 21, "Machanical Engineering")

student1.study()
student2.study()

student1.swim()
student2.swim()

student1.major_and_age()
student2.major_and_age()

class UBStudent(Student):
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm a studnet at {Student.university}")


student3 = UBStudent("John", 22, "Physics")
student3.say_hello()
student3.study()

#method overriding
class UBAStudent(Student):
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm a student at {Student.university}")

    def study(self): #this will override study method from the parent class
        print(f"{self.name} is studying in the library at {Student.university}.")

student4 = UBAStudent("Sheldon", 16, "Theoretical Physics")
student4.say_hello()
student4.study()

#encapsulating
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


