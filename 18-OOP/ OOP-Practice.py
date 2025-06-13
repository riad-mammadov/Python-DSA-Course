class Employee:
    
    numOfEmployees = 0
    raise_amount = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numOfEmployees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def raisePay(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 5:
            return False
        return True

emp1 = Employee('Riad','Mammadov', 60000)
emp2 = Employee('Test','User', 50000)
emp3 = Employee.from_string('James-Doe-60000')

import datetime
my_date = datetime.date(2024,7,13)

print(Employee.isWorkDay(my_date))