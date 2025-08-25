"""
Sample website login logic.
You can try how login works.
Example-ID : " student01 "
Example-PW : " 1234* "
"""

db_id = "student01"
db_pw = "1234*"

user_id = input(" Enter your ID: ")
user_pw = input(" Enter your Password: ")

if user_id == db_id and user_pw == db_pw:
    print(" Login Succsessful. ")
elif user_id != db_id:
    print(" ID does not exist.")
else:
    print(" Incorrect password.")

"""
Copyright (c) 2025 d7nsexii™

All rights reserved.
"""
