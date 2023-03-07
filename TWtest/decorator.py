def login_username(func):
    def user_name():
        input("Enter user name first")
        func()
    return user_name()    
@login_username
def login_passward():
    input("Enter passward--")