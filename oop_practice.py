#class employee:   ------------- class and object
#    pass

#employee1 = employee()
#employee1 = employee()

#print(type(employee1))

#class Employee: - constructor and self

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#employee1=Employee("yogesh", 25)
#employee2=Employee("Arun", 24)

#print(employee2.name)

#Attributes and Methods
#class Employees:

#    def __init__(self, name, age):
#        self.name=name
#        self.age=age
#    def display(self):
#        print(self.name)
#        print(self.age)

#employees1 = Employees("Yogesh", 25)
#employees1.display()

#Inheritance
#class Employee:

#    def display(self):
#        print("I am an employee")


#class Developer(Employee):

#    def coding(self):
#        print("I write Python code")


#developer1 = Developer()

#developer1.display()
#developer1.coding()

#All the concept covered in oops with example as below:
# 1. Parent Class
class Employee:

    # Constructor
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    # Display employee details
    def display(self):
        print(self.name)
        print(self.age)
        print(self.role)

    # Update employee role
    def update_role(self, new_role):
        self.role = new_role

    # Get employee name
    def get_name(self):
        return self.name

    # Get employee age
    def get_age(self):
        return self.age

    # Update employee age
    def update_age(self, new_age):
        self.age = new_age


# 2. Child Class
class Manager(Employee):

    # Method overriding
    def display(self):
        print("Manager Name:", self.name)
        print("Manager Age:", self.age)
        print("Manager Role:", self.role)

    # Manager's own method
    def conduct_meeting(self):
        print("Manager is conducting a meeting")


# 3. Create Employee Objects
employee1 = Employee("Yogesh", 25, "Developer")
employee2 = Employee("Arun", 26, "Tester")


# 4. Display Employees
print("===== Employee Details =====")
employee1.display()
employee2.display()


# 5. Update Employee Role
print("===== Updated Employee =====")
employee2.update_role("Senior Tester")
employee2.display()


# 6. Update Employee Age
employee2.update_age(35)


# 7. Get Employee Name and Age
print("===== Employee Name and Age =====")
print(employee1.get_name())
print(employee2.get_age())


# 8. Inheritance and Polymorphism
print("===== Manager Details =====")
manager1 = Manager("Arun", 35, "Manager")
manager1.display()
manager1.conduct_meeting()


# 9. Practice Challenge: Kumar
print("===== Kumar Details =====")

employee3 = Employee("Kumar", 28, "Tester")

employee3.update_role("Python Developer")

employee3.display()