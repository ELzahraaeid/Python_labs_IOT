import pwinput
import re
def login():
    mail_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    mail_flag = 0
    pass_flag = 0
    while True:
        if not mail_flag:
            email = input("Enter Your Email: ")
            if not (re.fullmatch(mail_regex, email)):
                print("Invalid Email syntax !!!!!")
                continue
            mail_flag = 1
        if not pass_flag:
            password = pwinput.pwinput(prompt='Enter Your Password: ', mask='*')
            if not password:
                continue
        break
    try:
        users_file = open("HelperFunctions\\Users.txt")
    except Exception as e:
        raise Exception(f"Error in Opening Users File : {e}")
    else:
        usersEmailsList = [(line.split(":"))[3] for line in users_file ]
        users_file.seek(0)
        usersEmails_pass_List = [(line.split(":"))[3:5] for line in users_file ]
        
        if email not in usersEmailsList:
            print("Email doesn't Exist......Try again..\n\n")
            return login()
            
        elif [email,password] in usersEmails_pass_List:
            print("successfully login.....")
            return usersEmails_pass_List.index([email,password])
        else:
            print("incorrect pass...Try again\n\n")
            return login()
        

        