from BusinessLogic.Manager import Person

class Dataguy:
    person1 = Person("Markus",21,"male")
    person2 = Person("Maria", 20, "female")

    person1.print_person_data()
    person2.print_person_data()
    print("hello world")
