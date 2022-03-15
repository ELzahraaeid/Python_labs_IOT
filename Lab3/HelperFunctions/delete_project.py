import json
import pandas as pd
from tabulate import tabulate

def Delete(user_id):
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
        file.close()
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
            
            
            file_data.pop(user_data_idx[int(row)])
            if len(file_data) > 0:
                try:
                    file = open("HelperFunctions\\projects.json","w")
                except Exception as e:
                    raise Exception(f"Error in Opening File : {e}")
                else:
                    json.dump(file_data[0], file)
                    file.write('\n')
                    file.close()
            else:
                try:
                    file = open("HelperFunctions\\projects.json","w")
                except Exception as e:
                    raise Exception(f"Error in Opening File : {e}")
                else: 
                    file.write('')
                    file.close()
            if len(file_data) > 1:
                try:
                    file = open("HelperFunctions\\projects.json","a")
                except Exception as e:
                    raise Exception(f"Error in Opening File : {e}")
                else:
                    for i in range(1,len(file_data)):
                        json.dump(file_data[i], file)
                        file.write('\n')
                    file.close()
            print("Data Deleted Successfully........")
                   
        else:
            print("No Existing Projects.....")
            file.close()