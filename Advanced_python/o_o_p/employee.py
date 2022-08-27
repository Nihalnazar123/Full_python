class Employee:
    def employedetails(self,name,emp_id,salary,designation,company_name):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
        self.designation=designation
        self.company_name=company_name
    def printemp(self):
        print('employee name : ',self.name)
        print('employee id : ',self.emp_id)
        print('salary : ',self.salary)
        print('designation : ',self.designation)
        print('company name : ',self.company_name)

emp1=Employee()
name=input('enter your name')
emp_id=int(input('enter your emp_id'))
salary=int(input('enter your salary'))
des=input('enter your place')
com=input('enter company name')
emp1.employedetails(name,emp_id,salary,des,com)
emp1.printemp()


emp2=Employee()
emp2.employedetails('nihal',27,28000,'kochi','google')
emp2.printemp()