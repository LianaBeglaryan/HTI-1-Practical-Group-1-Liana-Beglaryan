import re 
import sys    

def validate_phone_number(number):

    expression = '[0]?(([7]{2})|([5]{2})|(9(8|1)))((([-\ ][0-9]{2}){3})|(([-\ ][0-9]{3}){2}))'

    for symbol in number:
        if re.fullmatch(expression,symbol):
            print(True)
        else:
            print(False)


def validate_email(email): 
    
    regex = '^[a-z0-9]+[\-._+]?[a-z0-9]+[@]\w+[.]\w+$'

    if(re.search(regex,email)):  
        print(True)       
    else:  
        print(False) 



if __name__=='__main__':

    print(sys.argv)
    
    if validate_phone_number(sys.argv[1]):
       print("yes")
    else:
       print("no")   
       
   
    if validate_email(sys.argv[2]):
       print("yes")
    else:
       print("no")   

    
    
