# refactoring original task manager program and adding functions.

#================================= importing libraries =================================

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

#================================= read tasks =================================

#put read tasks into a function
def read_tasks():

    #create tasks.txt if it doesn't exist
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass

    #read task if a file is already available
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    task_list = []
    for t_str in task_data:
        curr_t = {}

        #split by semicolon and manually add each component and add to the curr_t dictionary
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False

        #append the the info from curr_t to the task_list list
        task_list.append(curr_t)

    return task_list


#================================= Login Section =================================

'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
#put login into a function
def login():

    #if no user.txt file, write one with a default account
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    #read in user_data
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    #convert to a dictionary
    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    #login false until user enters correct username and password
    logged_in = False

    #create title and ask user to enter their username and password
    while not logged_in:
        print(f"\n{lines}\n\t\tWelcome to the Task Manager. Please login to your account\
\n{lines}\n")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        
        #if username not in username keys then create error handling. let user know that 
        #the usernames can be case sensitive
        if curr_user not in username_password.keys():
            print(f"\n{stars}\n\t\t\t\tUsername not found\n\t\t\t\tUsernames are case \
sensitive\n{stars}")
            continue

        #create error handling for incorrect password
        elif username_password[curr_user] != curr_pass:
            print(f"\n{stars}\n\t\t\t\t\tIncorrect Password\n{stars}")
            continue

        #if correct username and password, log user in and continue with main program
        else:
            print("\nLogin Successful!")
            logged_in = True

            #return arguments for current user, current user is admin and username password 
            # dictionary
            return curr_user, curr_user == 'admin' , username_password


#=================================registering a user =================================

#create a register user function
def reg_user(username_password):

    while True:
        #request input of a new username
        new_username = input("New Username: ")

        #check if the new username already exists
        if new_username in username_password:
            print("ERROR: Username already in use. Please enter another Username")
            continue

        #request input of a new password
        new_password = input("New Password: ")

        #request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        #check if the new password and confirmed password are the same.
        if new_password == confirm_password:

            #if they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_data = []
                for k, v in username_password.items():
                    user_data.append(f"{k};{v}")
                out_file.write("\n".join(user_data))

            #exit the loop after successfully adding the user
            break  
        
        #error handling for incorrect password match.
        else:
            print("\nPasswords do not match")


#================================= adding a task =================================

#create an add task function
def add_task(task_list, username):

    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.
             - automatically show task completed as false'''
    
    #Get the current date.
    curr_date = date.today()
    
    #ask user to input a user the task is assigned to and allow them to cancel if they
    #decide not to add a task
    while True:
        task_username = input("\nName of person assigned to task (type '-1' to cancel): ")
        if task_username == "-1":
            print("\nTask canceled.")
            return
        
        #error handling if username not found
        elif task_username not in username_password.keys():
            print("\nUser does not exist. Please enter a valid username")
            continue
        
        #ask user to input title. or -1 to cancel adding a task
        task_title = input("\nTitle of Task (type '-1' to cancel): ")
        if task_title == '-1':
            print("Task canceled.")
            return
        
        #ask user to input description or -1 to canclel adding a task
        task_description = input("\nDescription of Task (type '-1' to cancel): ")
        if task_description == '-1':
            print("Task canceled.")
            return
        
        #ask user to input a due date or -1 to canclel adding a task
        while True:
            task_due_date = input("\nDue date of task (YYYY-MM-DD), (type '-1' to cancel): ")
            
            if task_due_date == '-1':
                print("\nTask creation canceled.")
                return

            
            try:
                #convert string to date time object and then take the date entry to error handle
                #if the user does not pick a date that is greater than the current date
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT).date()

                if due_date_time < curr_date:
                    print("\nDue date needs to be equal to or after todays date")
                    continue
                break

            #add error handling for incorrect date input
            except ValueError:
                print("\nInvalid datetime format. Please use the format specified")

        #create a dictionary for new task details
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        #append new task dictionary to the task list
        task_list.append(new_task)

        #write task list to tasks file in a list format seperated by ;
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                
                task_list_to_write.append(";".join(str_attrs))

            task_file.write("\n".join(task_list_to_write))
        
        #let user know tasks successfully added to the task file
        print("\nTask successfully added.")
        return


#================================= view all tasks =================================

#create a function to view all tasks
def view_all_tasks(task_list, curr_user):

    #if there are no tasks at all, advise user to add a task
    if not task_list:

        print(f"\n{stars}\nThere are no tasks to view.\nPlease consider adding a task from\
 the main menu\n{stars}")
        return

    #if there are tasks to show, print tasks out
    else:     
        '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)'''

        print(f"\n{lines}\n\t\t\t\t\tAll Tasks:\n{lines}")

        #enumerate tasks
        for option, t in enumerate(task_list, 1):

            #turn the boolean into a string so the user can see yes or no instead of true or false
            completed_task_stat = "Yes" if t['completed'] else "No"

            #display what is in the tasks
            disp_str = f"\n{lines}\nTask {option}: \t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Is the Task complete: \t {completed_task_stat}\n"
            disp_str += f"Task Description: \n{t['description']}\n{lines}\n"

            print(disp_str)
            
        
        #if a user does not have any tasks assigned to them and there are other tasks available,
        #they can add a task from all tasks as their own or return to the main menu
        while True:
            try:

                #display option menu for user
                all_tasks_menu = int(input('''Do you want to:\n
1. Assign a task from another user to yourself
2. Return to the main menu\n
Enter 1 or 2: '''))
                
                #call assign task to self function
                if all_tasks_menu == 1:
                    assign_task_to_self(task_list, curr_user)
                    return
                
                #exit to the main menu
                elif all_tasks_menu == 2:
                    return  
                
                #error handling for any other number than 1 or 2 selected
                else:
                    print("\nInvalid option selected.\n")
                    continue
            
            #error handling for anything other than a number selected
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        


#================================= view my tasks =================================

'''when user chooses this option display and enumerate all tasks and then ask if they want to 
edit a task or return to main menu:
user input = To edit a task enter the task number or enter -1 to return to the main menu

when a task is chosen, display task and give options to edit tasks:

1. edit username 
2. edit due date
3. mark as complete or incomplete
4. return to vm menu
5. return to main menu

if the task they choose is complete, display task and say task is complete and give option to 
return to main menu if they choose edit task. allow user to edit the due date or the username 
it's assigned to only. if they mark as complete offer a Y/N option:

1. type -1 to return to main menu'''


def view_my_tasks(task_list, curr_user, username_password):

    '''Reads the task from task.txt file and prints to the console in the 
format of Output 2 presented in the task pdf (i.e. includes spacing
and labelling)'''

    #get the current date.
    curr_date = date.today()
    
    #make sure tasks of the user are shown
    user_tasks = [task for task in task_list if task['username'] == curr_user]

    #if there are no tasks at all advise user to add tasks 
    if not task_list:

        print(f"\n{stars}\nThere are no tasks to view.\nPlease consider adding a task from\
 the main menu\n{stars}")
        return
    
    #if the user has no tasks, offer to add a task or change another users task as their own
    elif not user_tasks:

        while True:
            try:
                print(f"\n{stars}\nYou have no tasks assigned.\nPlease consider adding a task from\
 the main menu \nor changing tasks assigned to other users to yourself.\n{stars}\n")
                
                #display option menu for user
                no_task_menu = int(input('''Do you want to:\n
1. Assign a task from another users to yourself
2. Return to the main menu\n
Enter an option: '''))
                
                #call assign task to self function
                if no_task_menu == 1:
                    assign_task_to_self(task_list, curr_user)
                    return
                
                #exit to the main menu
                elif no_task_menu == 2:
                    return  
                
                #error handling for any other number than 1 or 2 selected
                else:
                    print("Invalid option selected.")
                    return
            
            #error handling for anything other than a number selected
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    #if the user has tasks then continue with the program    
    else:
        #print title
        print(f"\n{lines}\n\t\t\t\t\tYour Tasks:\n{lines}")

        #enumerate each task so that the user will be able to pick a task number in the next menus
        for option, t in enumerate(user_tasks, 1):
                
                #turn the boolean into a string so the user can see yes or no instead of true or 
                #false
                completed_task_stat = "Yes" if t['completed'] else "No"
                disp_str = f"\n{lines}\nTask {option}: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t\t {t['username']}\n"
                disp_str += f"Date Assigned: \t\t \
{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Is the Task complete: \t {completed_task_stat}\n"
                disp_str += f"Task Description: \n{t['description']}\n{lines}"
                    
                print(disp_str)

        #ask user if they want to edt a task
        while True:
            try:
                select_task = int(input("\nTo edit a task, enter the task number or Enter '-1' \
to return to main menu: "))
                if select_task == -1:

                    #return to main menu
                    return  
                
                #make sure task chosen is between all tasks given
                elif 1 <= select_task <= len(user_tasks):

                    #map the selected task to the original task list index so if any changes 
                    #are made the original task list will be modified too
                    selected_task = user_tasks[select_task - 1]
                    task_index = task_list.index(selected_task)

                    #if the task they choose is already completed offer to select another task
                    if task_list[task_index]['completed']:

                        print(f"\n{stars}\nThis task has already been completed and cannot be\
 edited.\n{stars}")

                        while True:
                            try:

                                #ask if they want to select another task or exit to the main menu
                                comp_task_menu = int(input('''Do you want to\n1. Select another task
2. Return to the main menu\n
Enter an option: '''))
                                #allow user to select another task
                                if comp_task_menu == 1:
                                    break

                                #exit to the main menu
                                elif comp_task_menu == 2:
                                    return  
                                
                                else:
                                    print("\nInvalid option selected.\n")
                                    continue

                            #error handling for anything other than a number selected
                            except ValueError:
                                print("\nInvalid input. Please enter a number.\n")

                    else:
                        #continue the loop to allow selecting another task
                        break

                #error handling if any other number slected
                else:
                    print("\nInvalid task selection. Please try again.\n")

            #error handling if a number is not selected
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        
        #continue with program to edit a task 
        while True:
            try:
                edit_choice = int(input(f'''\n{lines}\nChoose an option to edit the task:\n
1. Assign task to another user
2. Edit due date
3. Mark task as complete
4. Return to View My Tasks
5. Return to Main Menu
\nEnter Option: '''))
                
                 #assign this task to another user
                if edit_choice == 1:
                   
                    new_username = input(f"\n{lines}\nEnter the username to assign this task \
to (or enter '-1' to cancel): ")
                    
                    #return to the edit options
                    if new_username == '-1':
                        break

                    #change username if a username is found in task list and update task list
                    elif new_username in username_password:
                        task_list[task_index]['username'] = new_username
                        print(f"\n{lines}Task reassigned successfully.")
                    
                    else:
                        print(f"\n{stars}\nUsername not found. Please try again.\n{stars}\n")
                
                #edit due date
                elif edit_choice == 2:
                    while True:
                        new_due_date = input("\nEnter the new due date (YYYY-MM-DD), (or enter\
 '-1' to cancel): ")
                        
                        #return to the edit options
                        if new_due_date == '-1':
                            break 

                        #convert string to date time object and then take the date entry to 
                        #error handle if the user does not pick a date that is greater than 
                        #the current date
                        try:
                            chosen_due_date = datetime.strptime(new_due_date, "%Y-%m-%d").date()

                            #error handling if incorrect date chosen
                            if chosen_due_date < curr_date:
                                print("\nDue date needs to be equal to or after todays date")
                                continue  

                            #update new date in task list and return to editing menu
                            else:
                                task_list[task_index]['due_date'] = chosen_due_date
                                print("\nDue date updated successfully.")
                                break
                        
                        #error handling if incorect date format chosen
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")

                #mark task as complete
                elif edit_choice == 3:
                    completion_input = input("Mark task as complete? Enter 'yes' or\
 enter '-1' to cancel: ")
                    
                    #return to the edit options
                    if completion_input == '-1':
                        break
                    
                    #mark as complete if yes chosen
                    elif completion_input.lower() == 'yes':
                        task_list[task_index]['completed'] = True
                        print("\nTask marked as completed.")
                    
                    #error handling for incorect option chosen
                    else:
                        print(f"\n{stars}\nInvalid option. No changes made.\n{stars}")

                #view my tasks again and edit if needed. this allows user to view updated tasks 
                #after they have edited them
                elif edit_choice == 4:
                    return view_my_tasks(task_list, curr_user, username_password)

                #return to main menu
                elif edit_choice == 5:
                    return
                
                #error handling if incorrect number chosen
                else:
                    print("\nInvalid Choice. Please enter an option between 1-5")

                #save the updated task list back to the file
                with open("tasks.txt", "w") as file:
                    for task in task_list:
                        task_data = [
                            task['username'],
                            task['title'],
                            task['description'],
                            task['due_date'].strftime("%Y-%m-%d"),
                            task['assigned_date'].strftime("%Y-%m-%d"),
                            "Yes" if task['completed'] else "No"
                        ]
                        file.write(";".join(task_data) + "\n")

            except ValueError:
                print("\nPlease enter an option between 1-5.")
                

#================================= Assigning tasks =================================

#create a function to assign a task to yourself
def assign_task_to_self(task_list, curr_user):

    #display tasks that are not completed and assigned to other users
    other_users_tasks = [task for task in task_list if 
task['username'] != curr_user and not task['completed']]
    
    #error handling if there are no other tasks or all tasks are complete
    if not other_users_tasks:
        print("There are no tasks from other users available for re-assignment.")
        return
    
    #print title
    print(f"\n{lines}\n\t\t\t\tTasks available to re-assign\n{lines}\n")

    #enumerate tasks available
    for index, task in enumerate(other_users_tasks, 1):
        print(f"{index}. {task['title']} - Assigned to: {task['username']}")

    try:
        task_choice = int(input("\nSelect a task to assign to yourself (or enter\
 '-1' to cancel): "))
        
        #return to main menu if cancelled
        if task_choice == -1:
            return
        
        #make sure a task number is selected within the enumerated task range given
        elif 1 <= task_choice <= len(other_users_tasks):

            #map the selected task to the original task list index so if any changes 
            #are made the original task list will be modified too
            selected_task_index = other_users_tasks[task_choice - 1]
            original_index = task_list.index(selected_task_index)
            
            #modify changed username into the task list
            task_list[original_index]['username'] = curr_user

            print(f"\nTask '{task_list[original_index]['title']}' has been re-assigned to you.")
            
            # Save the updated task list back to the file
            with open("tasks.txt", "w") as file:
                for task in task_list:
                    task_data = [
                        task['username'],
                        task['title'],
                        task['description'],
                        task['due_date'].strftime("%Y-%m-%d"),
                        task['assigned_date'].strftime("%Y-%m-%d"),
                        "Yes" if task['completed'] else "No"
                    ]
                    file.write(";".join(task_data) + "\n")
        else:
            print("\nInvalid selection.")

    except ValueError:
        print("\nPlease enter a valid number.")


#================================= Generate task reports =================================

    '''selecting gr in the main menu will go through the generate task
    function AND the user task function. so make sure if the user is not admin to return 
    to main menu in both functions'''

#create a generate task function
def generate_task_report(task_list):

    #program will return to main menu and print error if user is not admin
    if not is_admin:
        print(f"\n{stars}\n\t\tYou do not have permission to view general reports.\n{stars}")
        return
    
    #calculate how many tasks in the task list
    total_tasks = len(task_list)

    #calculate how many completed tasks
    completed_tasks = sum(task['completed'] for task in task_list)

    #calculate how many uncompleted tasks
    uncompleted_tasks = total_tasks - completed_tasks

    #calculate overdue tasks
    overdue_tasks = sum(task['completed'] == False and task['due_date'] < datetime.now().date() for task in task_list)

    #find the percentage of incomplete tasks
    percentage_incomplete = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    #find the percentage of overdue tasks
    percentage_overdue = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    
    # Write to task_overview.txt 
    with open("task_overview.txt", "w") as file:
        file.write(f"Total number of tasks: {total_tasks}\n"
f"Total number of completed tasks: {completed_tasks}\n"
f"Total number of uncompleted tasks: {uncompleted_tasks}\n"
f"Total number of uncompleted tasks that are overdue: {overdue_tasks}\n"

#make sure percentageds are written to 2 decimal places
f"Percentage of tasks that are incomplete: {percentage_incomplete:.2f}%\n"
f"Percentage of tasks that are overdue: {percentage_overdue:.2f}%\n")
    
    print("\nReports generated successfully.")
    

#================================= Generate task reports =================================

def generate_user_report(task_list, users):

    #because the program runs through genrate task report first. there is no need for an 
    #error message. but an if not statement is needed if return to the main menu still
    if not is_admin:
        return

    #calculate total users
    total_users = len(users)

    #calculate total tasks
    total_tasks_generated = len(task_list)
    
    # create a user stat dictionary to count the statistics within the tasks
    user_stats = {user: {'total_assigned': 0, 'completed': 0, 'incomplete': 0, 'overdue': 0} 
for user in users}
    
    # Calculate stats for each user
    for task in task_list:
        user = task['username']

        if user in user_stats:
            user_stats[user]['total_assigned'] += 1

            if task['completed']:
                user_stats[user]['completed'] += 1

            else:
                user_stats[user]['incomplete'] += 1

                if task['due_date'] < datetime.now().date():
                    user_stats[user]['overdue'] += 1
    
    # Write to user_overview.txt
    with open("user_overview.txt", "w") as file:
        file.write(f"Total number of users registered: {total_users}\n"
f"Total number of tasks that have been generated: {total_tasks_generated}\n")
        
        #create a loop to gather users stats before writing to the user stats file
        for user, stats in user_stats.items():
            total_assigned = stats['total_assigned']
            completed = stats['completed']
            incomplete = stats['incomplete']
            overdue = stats['overdue']
            percent_of_total_tasks = ((total_assigned / total_tasks_generated) 
                                      * 100 if total_tasks_generated > 0 else 0)
            percent_completed = (completed / total_assigned) * 100 if total_assigned > 0 else 0
            percent_incomplete = (incomplete / total_assigned) * 100 if total_assigned > 0 else 0
            percent_overdue = (overdue / total_assigned) * 100 if total_assigned > 0 else 0
            
            #write the user stats to a file and then loop through the other users until 
            file.write(f"\nUser: {user}\n"
f"Total number of tasks assigned: {total_assigned}\n"

#make sure percentageds are written to 2 decimal places
f"Percentage of the total number of tasks: {percent_of_total_tasks:.2f}%\n"
f"Percentage of tasks completed: {percent_completed:.2f}%\n"
f"Percentage of tasks incomplete: {percent_incomplete:.2f}%\n"
f"Percentage of tasks overdue: {percent_overdue:.2f}%\n")
            
            

    


#================================= Display statistics =================================

#create a function to dislpay statistics
def display_statistics():
    
    #program will return to main menu and print error if user is not admin
    if not is_admin:
        print(f"\n{stars}\nYou do not have permission to view statistics.\n{stars}")
        return
    
    #call generate task and user reports so that if the user goes straight to ds option
    #they will get up to date reports
    generate_task_report(task_list)
    generate_user_report(task_list, username_password) 

    #open task overview file and print to terminal
    try:
        with open("task_overview.txt", 'r') as task_overview_file:
            print(f"\n{lines}\nTask Overview:\n{lines}")
            print(task_overview_file.read())

        #open user overview file and print to terminal    
        with open("user_overview.txt", 'r') as user_overview_file:
            print(f"\n{lines}\nUser Overview:\n{lines}")
            print(user_overview_file.read())

    #error handling if files not found
    except FileNotFoundError:
        print("\nReport files not found. Please generate reports first.")
    


#================================= Main Program =================================

#call main program
if __name__ == "__main__":

    #decorative variables
    lines = "-" * 100
    stars = "*" * 100

    #call the read tasks function and add to the task_list variable
    task_list = read_tasks()

    #call the login function and add data to the curr_user, is_admin and 
    #username_password vcariables
    curr_user, is_admin, username_password = login()
    
    while True:

        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.        
        menu = input(f'''\n{lines}\n\t\tSelect one of the following Options below:\n{lines}
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate Reports
ds - Display statistics
e - Exit
: ''').lower()

        #allow user to choose options which will then call specific functions. 
        if menu == 'r':
            reg_user(username_password)

        elif menu == 'a':
            add_task(task_list, curr_user)

        elif menu == 'va':
            view_all_tasks(task_list, curr_user)

        elif menu == 'vm':
            view_my_tasks(task_list, curr_user, username_password)

        elif menu == 'gr':
            generate_task_report(task_list)
            generate_user_report(task_list, username_password)

        elif menu == 'ds':
            display_statistics()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()
            
        else:
            print("\nInvalid option. Please Try again")