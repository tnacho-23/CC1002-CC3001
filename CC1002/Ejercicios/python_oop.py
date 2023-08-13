from calendar import weekday
from hashlib import new


class Employee:
#Class Variables
    nums_of_emps = 0
    raise_amount = 1.04

#Constructor/init method
    def __init__(self,first,last,pay): #self = instance
        #Atributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.nums_of_emps += 1

#Methods
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    
#Classmethods
    @classmethod    
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

#Staticmethods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True 
    

emp_1 = Employee('Juan', 'Molina', 1000)
emp_2 = Employee('Esteban','Claros', 50000)

#print(emp_1.first)
#print(emp_2.first)
#print(emp_1.fullname())
#print(emp_1.pay)

#emp_1.apply_raise()
#print(emp_1.pay)

#emp_1.raise_amount = 1.05
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#print(Employee.nums_of_emps)
#emp_3 = Employee('Lalo', 'Landa', 0)
#print(Employee.nums_of_emps)

#print(Employee.raise_amount)
#Employee.set_raise_amount(1.05)
#print(Employee.raise_amount)

#new_emp = Employee.from_string('Juanita-Alcachofa-3000')
#print(new_emp.fullname())

#import datetime
#my_date = datetime.date(2016, 7, 10)
#print(Employee.is_workday(my_date))

