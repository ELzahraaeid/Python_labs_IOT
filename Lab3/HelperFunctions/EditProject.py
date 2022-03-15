import json
import pandas as pd
from tabulate import tabulate
from datetime import datetime

def editing_menu():
    print("\n1)Edit Project TiTle\t\t\t\t2)Edit Project Details\n3)Edit Project Total Target\t\t\t4)Edit Project Start Date\n5)Edit Project End Date")
    while True:
        user_selection = input(">>>>Please Enter the Number Of the property that you want to edit: ")
        if user_selection == '1' or user_selection == '2' or user_selection == '3' or user_selection == '4' or user_selection == '5':
            break
        else:
            print(":')))))))))))) Please the choice must be number 1 or 2 or 3 or 4 or 5!!!!")

    return user_selection


def edit(user_id):
    try:
        file = open("HelperFunctions\\projects.json","r")
    except Exception as e:
        raise Exception(f"Error in Opening File : {e}")
    else:
        file_data = []
        user_data = []
        user_data_idx = []
        for idx,i in enumerate(file):
            obj = json.loads(i)
            if obj["id"] == user_id:
                user_data.append(obj)
                file_data.append(obj)
                user_data_idx.append(idx)
            else:
                file_data.append(obj)
        
        if user_data:
            df = pd.DataFrame(user_data)
            print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
            row = 0
            if len(user_data) > 1:
                while True:
                    row = input("Please Enter Project Number that You Want to Edit: ")
                    if row.isdigit():
                        if int(row) >= 0 and int(row) < len(user_data):
                            break
            file.close()
            item = editing_menu()
            attributes = {'1':'title', '2':'details', '3':'total_target','4':'start_date','5':'end_date'}
            format = "%d-%m-%Y"
            while True:
                new_data = input(f"Please Enter New project {attributes[item].capitalize()}: ")
                if (attributes[item] == "title" and new_data) or (attributes[item] == "details" and new_data) or (attributes[item] == "total_target" and new_data.isdigit()):
                    break
                elif (attributes[item] == "start_date"):
                    try:
                        bool(datetime.strptime(new_data, format)) 
                        if  new_data > file_data[user_data_idx[int(row)]]['end_date']:
                            print("The Start Date Should be Smaller Than The End Date!!!...")
                            continue
                    except:
                        print("Please Enter Valid Date!!!")
                        continue
                    break
                elif (attributes[item] == "end_date"):
                    try:
                        bool(datetime.strptime(new_data, format)) 
                        if  new_data < file_data[user_data_idx[int(row)]]['start_date']:
                            print("The End Date Should be Greater Than The Start Date!!!...")
                            continue
                    except:
                        print("Please Enter Valid Date!!!")
                        continue
                    break
            file_data.pop(user_data_idx[int(row)])
            
            try:
                file = open("HelperFunctions\\projects.json","w")
            except Exception as e:
                raise Exception(f"Error in Opening File : {e}")
            else:
                json.dump(file_data[0], file)
                file.write('\n')
                file.close()

            try:
                file = open("HelperFunctions\\projects.json","a")
            except Exception as e:
                raise Exception(f"Error in Opening File : {e}")
            else:
                for i in range(1,len(file_data)):
                    json.dump(file_data[i], file)
                    file.write('\n')
                file.close()
            print("Data Updated Successfully........")
            
            
            
        else:
            print("No Existing Projects.....")
            file.close()

    
    