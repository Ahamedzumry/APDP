class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print("name is ", self.name,"and salary is ",self.__salary)
# outside class
E = Employee("Abdullah",95000)
E.PrintName()
print(E.name)
print(E.printName())
print(E.__salary)