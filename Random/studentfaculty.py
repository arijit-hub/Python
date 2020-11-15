class institute_details(object):
    def __init__(self):
        self.name=input('Enter the name')
        self.address=input('Enter the address')
        self.phone=input('Enter phone number')
        self.email=input('Enter email id')

    def change_name(self,new_name):
        self.name=new_name

    def change_address(self,new_address):
        self.address=new_address
    def change_phone(self,new_phone):
        self.phone=new_phone
    def change_email(self,new_email):
        self.email=new_email
    


class student(institute_details):
    def __init__(self):
        super().__init__()
        self.roll_number=input('Enter the roll number')
        self.course=input('Enter course')

    def display_details(self):
        print(self.name,self.address,self.phone,self.email,self.roll_number,self.course)

class faculty(institute_details):
    def __init__(self):
        super().__init__()
        self.employee_id=input('Enter Employee Id')
        self.department=input('Specialization')
    def display_details(self):
        print(self.name,self.address,self.phone,self.email,self.employee_id,self.department)



person=input('Are you a student or a faculty?')

if person=='student':
    student1=student()
    

elif person=='faculty':
    faculty1=faculty()
        
    
