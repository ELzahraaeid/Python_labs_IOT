from HelperFunctions.createProj import createP
from HelperFunctions.viewProjs import viewP
from HelperFunctions.EditProject import edit
from HelperFunctions.delete_project import Delete
def secMenu(id):
    print("\n--------------------------------- Project Menu -----------------------------------")
    print("\n\t\t\t\t1)Create Project\n\t\t\t\t2)View All Projects\n\t\t\t\t3)Edit Projects\n\t\t\t\t4)Delete Project\n")
    while True:
        user_selection = input(">>>>Please Enter the Number Of Choice: ")
        if user_selection == '1' or user_selection == '2' or user_selection == '3' or user_selection == '4':
            break
        else:
            print(":')))))))))))) Please the choice must be number 1 or 2 or 3 or 4 !!!!")
    
    match user_selection:
        case '1':
           createP(id)
        case '2':
           viewP()
        case '3':
            edit(id)  
        case '4':
            Delete(id)
    secMenu(id)      