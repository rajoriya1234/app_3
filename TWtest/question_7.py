# WAP to manage ATM opreation
class PinError(Exception):
    pass

class OptionError(Exception):
    pass


by_defaut_amount = 2000
def check_amount():
    print(by_defaut_amount)
def option_menu():
    print("Please Choose the Option Below")
    print("Option -- C for Credit Amount")
    print("Option -- D for Debit Amount")
    print("Option -- B for Check Balance Amount")
    print("Option -- R for Repeat the Process")
    print("Option -- E for Exit")
    try:
        user_input = input("Choose --")
        case_change = user_input.upper()
        if user_input.isalnum:
            raise OptionError
        elif case_change == "B":
            check_amount()    
    except OptionError:
        print("Enter the right Option")     

def get_pin():
    num_of_time_get_pin = 0

    while num_of_time_get_pin < 3:

        try:
            input_pin = input("Enter your pin code--")
            strings = str(input_pin)
        
            if len(strings) == 6 and input_pin.isalnum:
                option_menu()
                break

            else:
                num_of_time_get_pin+=1
                raise PinError
            
        except PinError:
            print("Pin is Not Vailid")         

get_pin()    