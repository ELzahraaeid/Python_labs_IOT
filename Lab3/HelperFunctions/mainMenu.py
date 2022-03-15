from HelperFunctions.registration import Regist
from HelperFunctions.login import login
from HelperFunctions.secMenu import secMenu
def mainMenu():
    print("\n1)Registration\t\t2)login\n")
    while True:
        user_selection = input(">>>>Please Enter the Number Of Choice: ")
        if user_selection == '1' or user_selection == '2':
            break
        else:
            print(":')))))))))))) Please the choice must be number 1 or 2 !!!!")
    
    match user_selection:
        case '1':
            Regist()
            mainMenu()
        case '2':
            id = login()
            secMenu(id)
            
