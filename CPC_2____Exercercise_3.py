# Range of classes to classify 
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def __repr__(self):
        return self._name + " has a salary of " + "{:.2f}".format(self._salary)

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return self._name + " has a salary of  " + "{:.2f}".format(self._salary) + " and manages the " + self._department + " department"

class Executive(Manager):

    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def __repr__ (self):
        return self._name + " has a salary of " + "{:.2f}".format(self._salary) + " and the executive for the " + self._department + " department"


# Declaring more classes form classes about people in different social classes who were probably in the same class
emp = Employee("Jack Von", 420.00)
man = Manager("James Miles", 720.00, "Computer")
exe = Executive("Neo DiCarpio", 90000.00, "Monkey Makers")

# Main Programin
class main:
    print(emp)
    print(man)
    print(exe)


main()