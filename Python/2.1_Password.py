def check_length(password):
    if(len(password)<10):
        print("The password should atleast contain 10 characters long.")

def check_upper(password):
    count=0
    for char in password:
        if char.isupper():
            count+=1
    if count<2:
            print("The password should atleast contain two capital letters.")

def check_lower(password):
    count=0
    for char in password:
        if char.islower():
            count+=1
    if count<2:
            print("The password should atleast contain two lower case letters.")

def check_numbers(password):
    count=0
    for int in password:
          if int.isdigit():
               count+=1
    if count<2:
         print("The password should atleast contain two digits.")

def check_special(password):
    count=0
    for char in password:
        if char in ['@','#','$','%','&','*','!']:
            count+=1
    if count<2:
         print("The password should atleast contain two special characters.")

def check_sequence(username,password):
    username = username.lower()
    for i in range(len(password) - 2):
        substring = password[i:i+3]
        if substring.lower() in username:
            print("The password should not contain any sequence of three or more consecutive characters from the username")
            break

def check_repetition(password):
    for i in range(len(password)-3):
        if password[i:i+4] ==  password[i] * 4:
            print("The password should not contain any character repeating 3 or more times in next to it.")

def check_old(password,old_passwords):
     for i in range(len(old_passwords)):
          if password == old_passwords[i]:
            print("The password should not be same as one of the old passwords.")
            break

username=input("Enter the username ")
password=input("Enter the password ")
old_password1=input("Enter the old password 1 ")
old_password2=input("Enter the old password 2 ")
old_password3=input("Enter the old password 3 ")
old_passwords=[old_password1,old_password2,old_password3]
check_length(password)
check_upper(password)
check_lower(password)
check_numbers(password)
check_special(password)
check_sequence(username,password)
check_repetition(password)
check_old(password,old_passwords)
