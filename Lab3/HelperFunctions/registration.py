import re
import pwinput
# import getpass
############################### validation functions #########################
def UserName(which_name):
    while True:
        name = input(f"Enter Your {which_name}: ")
        if name.isalpha():
            break
        else:
            print("please Enter Correct Name!!!!!!!!!!!")
    return name

def UserMail():
    mail_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    try:
        users_file = open("HelperFunctions\\Users.txt")
    except Exception as e:
        raise Exception(f"Error in Opening Users File : {e}")
    else:
        usersEmailsList = []
        if users_file.read(1):
            users_file.seek(0)
            usersEmailsList = [(line.split(":"))[3] for line in users_file ]
        while True:
            email = input("Enter Your Email: ")
            if not (re.fullmatch(mail_regex, email)):
                print(":')))))) Invalid Email   Try Again!!!!!!!!")
                continue
            elif email in usersEmailsList:
                print(":')))))) This Email already Exist   Try Again!!!!!!!!")
                continue
            else:
                users_file.close()
                break
    return email, len(usersEmailsList)
        
def UserPassword():
    # p = getpass.getpass(prompt='Please Enter a Password:  ')
    while True:
        password = pwinput.pwinput(prompt='Please Enter a Password: ', mask='*')
        if len(password) < 5:
            print("Password does't be less than 5 letters!!!!!!!")
            continue
        elif ":" in password:
            print("Attention:  The password can't contain ':'")
            continue
        else:
            confirmPass = pwinput.pwinput(prompt='Confirm the Password: ', mask='*')
            if password == confirmPass:
                break
            else:
                print("!!!!!!!!!! Try Again.......")
                continue
    return password

def UserPhone():
    while True:
        phone = input("Enter Phone Number: +01")
        if phone.isdigit and len(phone) == 9 and ":" not in phone:
            break
    return phone
################################# Register Function ##########################
def Regist():
    fname = UserName("First Name")
    lname = UserName("Last Name")
    email, id = UserMail()
    password = UserPassword()
    phone = UserPhone()
    try:
       file = open("HelperFunctions\\Users.txt", "a")
    except Exception as e:
        raise Exception(f"Error in Opening File : {e}")
    else:
        record = str(id) + ":" + fname + ":" + lname + ":" + email + ":" + password + ":01" + phone + '\n'
        file.write(record)
        print("congratulation ..Registration done successfully..\n")
        print("Now .. You can login The system...")
        file.close()

    

