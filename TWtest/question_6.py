#WAP to vaildate mobile number using the Exception
class NotVailidNumberError(Exception):
    pass
class NumberError(Exception):
    pass
class Error(Exception):
    pass

input_num = input("Enter mobile number--")
lenght = len(input_num)

try:
    if int(input_num[0]) > 5 and lenght == 10:
        print("Number is Accepted")
        
    elif lenght < 10 or lenght > 10:
        raise NumberError 
    
    elif int(input_num[0]) < 6:
        raise NotVailidNumberError
    
    elif input_num.isalpha():
        raise Error
    
except NumberError:
    print("Your Should be 10 digit")
except NotVailidNumberError:
    print("Your Number is not Vailid")    
except Error:
    print("not a string only number")         
       
