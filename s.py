class Employee(object):

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.fist = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees = employees

        def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)
        
        def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)

        def print_emps(self):
            for emp in self.employees:
                print "--->", emp.fullname()

dev_1 = Developer("justin", "bieber", 10000, 'c++')
dev_2 = Developer("taylor", "swift", 2000, 'python')

m1=Manager("elon", "musk", 10000, [dev_1])
print m1.email

# print dev_1.email
# print dev_1.prog_lang