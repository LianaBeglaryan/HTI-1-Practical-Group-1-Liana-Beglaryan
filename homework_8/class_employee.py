import re
import datetime

class Employee:

    def __init__(self, first_name , last_name , full_name ,gender , phone_number , work_email ,join_date, leave_date ,salary , trial_passed = True):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.gender = gender
        self.phone_number = phone_number 
        self.work_email = work_email
        self.trial_passed =  trial_passed
        self.join_date = join_date
        self.leave_date = leave_date
        
        self.salary = salary 
        
    def validate_email(self): 

        regex = '^[a-z0-9]+[\-._+]?[a-z0-9]+[@]\w+[.]\w+$'

        if(re.search(regex,self.work_email)):  
            return self.work_email 
        else:  
            print("Your email address is not valid") 


    def validate_phone_number(self):
        expression = '^[0]?(([7]{2})|([5]{2})|(9(8|1)))((([-\ ][0-9]{2}){3})|(([-\ ][0-9]{3}){2}))'
        for symbol in self.phone_number:
            if re.fullmatch(expression,self.phone_number):
                return self.phone_number
            else:
                print("Your phone number is false") 
                break        
    
    def trial(self):
        if self.trial_passed == False:
            print("The trial is not passed")
        else :
            print("Yes")    

    def __repr__(self):
        return f'{self.first_name},{self.last_name},{self.full_name},{self.gender},{self.phone_number},{self.work_email},{self.trial_passed},{self.join_date},{self.leave_date},{self.salary}' 



emp =  Employee('Lianch' , 'Beglaryan',' Liana Beglaryan ','F', "077 25 27 29" , "li.beglaryan@mail.ru", False, "01.12.2019", "15.01.2021" , '200$' )

print(emp)

print(emp.validate_email())
  
print(emp.validate_phone_number())

print(emp.trial())

