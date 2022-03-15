import json
import pandas as pd
from tabulate import tabulate
def viewP():
    try:
        file = open("HelperFunctions\\projects.json")
    except Exception as e:
        raise Exception(f"Error in Opening File : {e}")
    else:
        data = []
        for i in file:
            obj = json.loads(i)
            data.append(obj)
        if data:
            df = pd.DataFrame(data)
            print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
        else:
            print("No Existing Projects.....")
        