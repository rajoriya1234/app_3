# write a program to check common letter in two input string

first_input = input("enter first input--")
second_input = input("enter second input--")
print({first_str for first_str in first_input for second_str in second_input if first_str == second_str})