# object oriented programing variables
# they are divided into two types
# static and instance

# static variable is related to class and we call static variable using class name
# instance variable is related to methods and we call static variable using self.
# eg:


class Employee:
    company_name='google'
    def employedetails(self,name,emp_id,salary,designation):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
        self.designation=designation
    def printemp(self):
        print('employee name : ',self.name)
        print('employee id : ',self.emp_id)
        print('salary : ',self.salary)
        print('designation : ',self.designation)
        print('company name : ',Employee.company_name)

emp1=Employee()
name=input('enter your name')
emp_id=int(input('enter your emp_id'))
salary=int(input('enter your salary'))
des=input('enter your place')
emp1.employedetails(name,emp_id,salary,des)
emp1.printemp()


emp2=Employee()
emp2.employedetails('nihal',27,28000,'kochi')
emp2.printemp()