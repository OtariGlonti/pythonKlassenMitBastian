class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_person_data(self):
        print("person name is: " + self.name + ". Age is " + str(self.age) +  "and gender is: " + self.gender)
        
person1 = Person("Markus",21,"male")
person2 = Person("Maria", 20, "female")

person1.print_person_data()
person2.print_person_data()