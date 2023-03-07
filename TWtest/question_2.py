# Write a program to create a diamond pattern in python using a single loop
star_range = 10
for star in range(1,star_range):
    if star < star_range//2:
        print(" "*(star_range-star)+" *"*(star))
    else:
        print(" "*(star)+" *"*(star_range-star))