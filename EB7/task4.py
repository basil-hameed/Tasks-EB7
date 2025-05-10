
"""
Input 
A list of values
my_list = [10, 501, 22, 37, 100, 999, 87, 351] 

Logical 

number % 2  == 0 (Even)

Output

Even list and Odd list

"""
my_list = [10, 501, 22, 37, 100, 999, 87, 351] 

# using for loop to iterate the values
for number in my_list:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

