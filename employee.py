class Employee :
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        print(self.position,"is earning",self.salary)

employee1 = Employee("John","CEO",350000)
print (employee1.name, employee1.position, employee1.salary)
employee1.info()
employee2 = Employee("Kate","Treasure",350000)
employee3 = Employee("Mike","Board Chairman",350000)
employee4 = Employee("Benny","Operation Manger",350000)
employee5 = Employee("Liam","Chief surgeon",350000)
employee6 = Employee("Sir","Club secretary",350000)