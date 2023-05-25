import os

def log_data(k):
    parent_folder_path = "C:/Users/kshah/OneDrive/Desktop/projects"
    folder_name = k + "-report"
    path_join = os.path.join(parent_folder_path, folder_name)

    is_folder_exist = os.path.exists(path_join)
    if is_folder_exist:
        print("Folder Already Exist")
    else:
        os.mkdir(path_join)
        print("folder created", folder_name)

        activity = int(input("Enter 1 for EXCERSISE and 2 for FOOD: "))
        if(activity == 1):
            value = input("type here\n")
            log_food_report = open(k + "-ex.txt", "a")
            log_food_report.write(value)
            log_food_report.close

        elif(activity == 2):
            value = input("type here\n")
            log_food_report = open(k + "-food.txt", "a")
            log_food_report.write(value)
            log_food_report.close
        else:
            print("Please Choose Valid option")
    


def retrieve_data(k):
    parent_folder_path = "C:/Users/kshah/OneDrive/Desktop/projects"
    folder_name = k + "-report"
    path_join = os.path.join(parent_folder_path, folder_name)
    is_folder_exist = os.path.exists(path_join)

    if is_folder_exist:
        activity = int(input("Enter 1 for EXCERSISE and 2 for FOOD: "))
        if(activity == 1):
            retrieve_ex_report = open(k + "-ex.txt", "r")
            content = retrieve_ex_report.read()
            print(content)
            retrieve_ex_report.close
        
        elif(activity == 2):
            retrieve_food_report = open(k + "-food.txt", "r")
            content = retrieve_food_report.read()
            print(content)
            retrieve_food_report.close
        else:
            print("Please Choose Valid Option")

    else:
        print("Folder dosent exist")

    
    

print("HEALTH MANAGEMENT SYSTEM")
input_data = int(input("Press 1 for LOG the value and 2 for RETRIEVE: "))

if input_data == 1:
    patient_name = str(input("Enter patient name to LOG the data: "))
    log_data(patient_name)
elif input_data == 2:
    patient_name = str(input("enter patient name to RETRIEVE details: "))
    retrieve_data(patient_name)
else:
    print("Please Choose Valid Option")

