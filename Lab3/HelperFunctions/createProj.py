import json
from datetime import datetime
def createP(user_id):
    while True:
        title = input("Please Enter Project Title: ")
        if  title :
            break
    while True:
        details = input("Please Enter Project Details: ")
        if  details :
            break
    
    while True:
        target = input("Please Enter Project Total Target: ")
        if  target.isdigit() and target:
            break
    while True:
        format = "%d-%m-%Y"
        S_date = input("Please Enter Campaign Start Date: ")
        try:
            bool(datetime.strptime(S_date, format)) 
            break
        except:
            print("Please Enter Valid Date!!!")
            continue
    while True:
        format = "%d-%m-%Y"
        E_date = input("Please Enter Campaign End Date: ")
        try:
            bool(datetime.strptime(E_date, format)) 
            if not E_date > S_date:
                print("The End Date Should be Greater Than The Start Date!!!...")
                continue
            break
        except:
            print("Please Enter Valid Date!!!")
            continue

    dictionary = {
    "id" : user_id,
    "title" : title,
    "details" : details,
    "total_target" : target,
    "start_date" : S_date,
    "end_date" : E_date
    }
    with open("HelperFunctions\\projects.json", "a") as file:
        json.dump(dictionary, file)
        file.write('\n')
  