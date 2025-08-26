#Discount rate calculator
# * this calculator only support basic calculaition *
#Enter the price, and discount rate
#And just see the result!

un = input("Enter your name : ")
price = int(input("Enter the price : " ))
discount = float(input("Enter the discount rate (%) : " ))

final_price = price - (price * discount / 100)
print(f"{un}, Final Price is {final_price}!")


"""
Copyright (c) 2025 d7nsexii™

All rights reserved.
"""


