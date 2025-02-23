class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"My name is {self.name}.")

class Student(Person):
    def __init__(self,name,age,school_year,favourite_sport):
        super().__init__(name)
        self.age = age
        self.school_year = school_year
        self.favourite_sport = favourite_sport
    
    def show_details(self):
        print("The details of the student are: ")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"school_year: {self.school_year}")
        print(f"favourite_sport: {self.favourite_sport}")

"""Creating the instance of the class"""
student1 = Student("Jack",12,"Year 7","Badminton")

student1.greet()
student1.show_details()