"""
Accept five hobbies form the user and write in a file 'hobby.txt'
each hobby should wrtie in a separate line
without using the write() function 
""" 

    
def user_hobbies(hobby,num):
    #print(hobby)
    with open('hobby.txt','a+') as hobbies_file:    
        hobbies_file.writelines(f"\nuser--{num} hobby is {hobby}\n")
          
hobby = 1       
while hobby <= 5:
    print(f"Enter Your--{hobby} hobby")
    user_hobby = input("Write hobby--")
    call_func = user_hobbies(user_hobby,hobby)
    hobby+=1
        