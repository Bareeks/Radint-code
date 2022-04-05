# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print(name + ' likes ' + favorite_color)

# x = 10
# x += 4
# print(x)

# price = 1000000
# good_credit = False

# if good_credit:
#     print('down payment is', 0.1 * price)
# else:
    # print('down payment is', 0.2 * price)
    
name = input("Create a Username ")
 
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")