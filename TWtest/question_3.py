# write a program in python to read the first 5 characters from the file

# create a file with some data 

with open ('data.text','r') as f:
    print(f.read(5))
    
    # for value in f:
    #     leghth = len(value)
        
    #     ans_list = [value[single_value] for single_value in range(leghth) if single_value <= 4]
            
    #     print(ans_list)
       
    # count_charactor = f.readline(5)
    # print(count_charactor)        
                 