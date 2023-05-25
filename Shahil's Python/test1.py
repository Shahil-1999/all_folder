import os
import shutil
from test import create 

def log_record():
    create(1, 'ravi', 'lal', 'gobra', 7)


log_record()
    # directory_name = name + "-report"
    # is_dir_created = create_directory(directory_name, False)

    # if(is_dir_created):
    #     print("Record already exists for this Patient in our Database!!")
    # else:
    #     print("Record doesn't exists for this Patient.Creating new Record!!")  


    #     log_option = int(input("Press 1.To LOG FITNESS Record 2.To LOG HEALTH Record: "))   
    #     if(log_option == 1):
    #         activity = int(input("Press 1.To LOG WORKOUT Details 2.To LOG DIET PLAN Details: "))
    #         fitness_directory_name = name + "-fitness-report"
            
    #         is_fitness_dir_created = create_directory(directory_name, fitness_directory_name)
                        
    #         print(is_fitness_dir_created)
    #         if(is_fitness_dir_created):
    #             print("FITNESS Directory for this Patient already exists in our Database!!")
    #         else:
    #             print("Fitness Record doesn't exists for this Patient.Creating new Record!!")
    #             parent_fitness_dir_path = r'C:/Users/kshah/Downloads/Final-Year-Python-Project (1)/Final-Year-Python-Project/'+directory_name+'/'+fitness_directory_name+'/'
    #             if(activity == 1):
    #                         # Directory
    #                 workout_data = input("Type your WORKOUT Plan here.....\n")
    #                 workout_record_name='workout-report.txt'
    #                 create_workout_record=create_record(parent_fitness_dir_path, workout_record_name, workout_data)
    #                 print("Workout Details successfully Logged in the Database")
    #             elif(activity == 2):
    #                 diet_data = input("Type your DIET Plan here.....\n")
    #                 diet_record_name='diet-report.txt'
    #                 create_diet_record=create_record( parent_fitness_dir_path, diet_record_name, diet_data)
    #                 print("Diet Plan Details successfully Logged in the Database")
    #             else:
    #                 print("Please Choose Valid Activity option")
                        
    #     elif(log_option == 2):
    #         health_measures = int(input("Press 1.To LOG BODY TEMPERATURE Details 2.To LOG DIABETES Details 3.To LOG BREAST CANCER Details: "))
    #         if(health_measures == 1):  
    #             body_temp = float(input("Please enter Patient's Body Temperature: "))
    #             if(body_temp>97.4):
    #                 print("Patient is suffering from FEVER Current Body Temperature: "+body_temp)
    #             else:
    #                 print("Patient Body Temperature is NORMAL")         
    #     else:
    #         print("Please Choose Valid Fitness option")


#____________________________________________________________________________________________________________________________________________________________________


# def retrieve_record(name):
#     directory_name = name + "-report"
#     is_dir_created=show_directory(directory_name, False)
#     if(is_dir_created):
#         print("Record exists for this Patient in the Database!!")  
#         log_option = int(input("Press 1.To RETRIEVE FITNESS Record 2.To RETRIEVE HEALTH Record: "))   
#         if(log_option == 1):
#             activity = int(input("Press 1.To RETRIEVE WORKOUT Details 2.To RETRIEVE DIET PLAN Details: "))
#             fitness_directory_name = name + "-fitness-report"
            
#             is_fitness_dir_created = show_directory(directory_name, fitness_directory_name)
                        
#             print("is_fitness_dir_created",is_fitness_dir_created)
#             if(is_fitness_dir_created):
#                 print("FITNESS Directory for this Patient exists in our Database!!")
#                 parent_fitness_dir_path=r'C:/Users/kshah/Downloads/Final-Year-Python-Project (1)/Final-Year-Python-Project/'+directory_name+'/'+fitness_directory_name+'/'
#                 if(activity == 1):
#                             # Directory
#                     workout_record_name='workout-report.txt'
#                     print('parent_fitness_dir_path',parent_fitness_dir_path)
#                     show_workout_record=show_record(parent_fitness_dir_path, workout_record_name)
#                     print("Workout Details successfully Retrieved from the Database")
                            
#                 elif(activity == 2):
#                     diet_record_name='diet-report.txt'
#                     show_diet_record=show_record(parent_fitness_dir_path, diet_record_name)
#                     print("Diet Plan Details successfully Retrieved from the Database")
#                 else:
#                     print("Please Choose Valid Activity option")
#             else:
#                 print("Fitness Record doesn't exists for this Patient in our Database!!")
#                         # parent_fitness_dir_path=r'C:/Users/shiwa/Documents/Final-Year-Python-Project/'+directory_name+'/'+fitness_directory_name+'/'
                       
                        
#         elif(log_option == 2):
#             health_measures = int(input("Press 1.To RETRIEVE BODY TEMPERATURE Details 2.To RETRIEVE DIABETES Details 3.To RETRIEVE BREAST CANCER Details: "))
#             if(health_measures == 1):  
#                 body_temp = float(input("Please enter Patient's Body Temperature"))
#                 if(body_temp > 97.4):
#                     print("Patient is suffering from FEVER Current Body Temperature: "+body_temp)
#                 else:
#                     print("Patient Body Temperature is NORMAL")         
#         else:
#             print("Please Choose Valid Fitness option")
#     else:
#         print("Record doesn't exists for this Patient in the Database!!")
 

# def create_directory(directory_name, sub_dir_name) :
#     parent_dir = "C:/Users/kshah/Downloads/Final-Year-Python-Project (1)/Final-Year-Python-Project"
#     if(sub_dir_name):
#         parent_dir = parent_dir +'/'+ directory_name
#         print('parent_dir', parent_dir)
#         path = os.path.join(parent_dir, sub_dir_name)
#     else:
#         print('parent_dir', parent_dir)
#         path = os.path.join(parent_dir, directory_name)
#     print(path)
#     is_dir_exist = os.path.exists(path)
#     print(is_dir_exist)
#     if(is_dir_exist):
#         return True
#     else: 
#         os.mkdir(path)
#         print("Directory  created", directory_name)
#         return False


# def create_record(final_dir_path,file_name,user_data) :
#     final_file_path= final_dir_path+file_name
#     is_file_exist = os.path.exists(final_file_path)
#     print( is_file_exist)
#     if(is_file_exist):
#         return True
#     else:
#         print(final_file_path)
#         with open(final_file_path, 'w') as fp:
#             fp.write(user_data)
#             fp.close()
#             return False 


# def show_directory(directory_name,sub_dir_name):
#     print('directory_name,sub_dir_name',directory_name,sub_dir_name)
#     parent_dir = "C:/Users/kshah/Downloads/Final-Year-Python-Project (1)/Final-Year-Python-Project"
#     if(sub_dir_name):
#         parent_dir= parent_dir+'/'+directory_name
#         print('parent_dir', parent_dir)
#         path = os.path.join(parent_dir, sub_dir_name)
#     else:
#         print('parent_dir', parent_dir)
#         path = os.path.join(parent_dir, directory_name)
#         # Path
       
#     print("path",path)
#     is_dir_exist = os.path.exists(path)
#     print(is_dir_exist)
#     if(is_dir_exist):
#         return True
#     else: 
#         return False
       

# def show_record(final_dir_path,file_name):
#     print("Show record.........")
#     print('final_dir_path,file_name',final_dir_path,file_name)
#     final_file_path= final_dir_path+file_name
#     is_record_exist = os.path.exists(final_file_path)
#     print(is_record_exist)
      
#     if(is_record_exist):
#         print("Record exists for this Patient in our Database!!")
#         with open(final_file_path, 'r') as fp:
#             content = fp.read()
#             print(content)
#             fp.close()
#             return True
#     else:
#         print("No Record exists for this Patient in the Database!!")
#         return False
                 

# def delete_record(name):
#     directory_name = name + "-report"
#     parent_dir = "C:/Users/kshah/Downloads/Final-Year-Python-Project (1)/Final-Year-Python-Project"
#     is_dir_Exists=show_directory(directory_name, False)
#     if(is_dir_Exists):
#         print("Record exists for this Patient in our Database!!")
#         path = os.path.join(parent_dir, directory_name) 
#         # removing directory 
#         shutil.rmtree(path)
#     else:
#          print("No Record exists for this Patient in the Database!!")


# print("Welcome to HEALTH MONITORING SYSTEM of CITY Hospital!!")
# input_data = int(input("Press 1.To LOG Patient Details 2.To RETRIEVE Patient Details 3.To DELETE Patient Details: "))

# if input_data == 1:
#     patient_name = str(input("Enter patient name to LOG the data: "))
#     log_record(patient_name)
# elif input_data == 2:
#     patient_name = str(input("Enter patient name to RETRIEVE the details: "))
#     retrieve_record(patient_name)
# elif input_data == 3:
#     patient_name = str(input("Enter patient name to DELETE the details: "))
#     delete_record(patient_name)
# else:
#     print("Please Choose Valid Option")