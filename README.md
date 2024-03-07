Capstone Project - Lists, Functions, and String Handling - Software Engineering Bootcamp

For this Task, I had to use lists or dictionaries and functions to extend the
functionality of a simple task management system. This is a program designed for
a small business to help it manage tasks assigned to each member of a team

My main focus was to:

1. Remove all syntax, runtime, and logical errors from the code.

2. Create functions to perform specific units of work.

3. Make sure that the code is readable.

4. Make sure that the code is as efficient as possible. 

5. Make sure that all output that my program provides to the user is easy to
read and understand


--------------------------------Table of Contents-------------------------------------

1.0: Installing the Program

1.1: Setting Up Visual Studio Code

1.2: Running the Program

2.0: Using the Program

3.0: Original Code

4.0: Credits

--------------------------------------------------------------------------------------

(1.0)--------------------------------Installing the Program---------------------------

Requirements:

Visual Studio Code: Ensure that Visual Studio Code is installed on your computer.

Git (Optional): If the project is hosted on GitHub and users will clone the repository, they should have Git installed. Download it from https://git-scm.com/.

Python: The project is written in Python, ensure it is installed and properly configured on your system.

Downloading the Project
Clone the Repository: Open a terminal or command prompt and run the following command to clone the GitHub repository:

EXAMPLE: 

git clone https://github.com/username/project-name.git

Replace example with the actual URL of the project's repository.

Alternatively, Download Manually: If not cloning, you can download the project manually by navigating to the GitHub repository in a web browser, clicking the "Code" button, and selecting "Download ZIP". After downloading, unzip the folder to a desired location.


(1.1)-------------------------------Setting Up Visual Studio Code---------------------

Open the Project in VSCode: Launch VSCode, go to "File" > "Open Folder", and select the project folder that you cloned or downloaded and unzipped.

Install Required Extensions: 

1. GitHub Pull Requests
2. Pylance
3. Python


(1.2)-------------------------------Running the Program-------------------------------

Terminal: Open the integrated terminal in VSCode by selecting "Terminal" > "New Terminal" from the menu bar. Then run the program by typing the appropriate command (e.g., python script_name.py) and pressing Enter.




(2.0)-------------------------------Using the Program---------------------------------

To start the program, login as the default user. 
The default username is: "admin"
The default password is: "password"
you can then start adding tasks or new users as required.

![img](https://private-user-images.githubusercontent.com/151395535/310897977-22e55b78-4345-4ff4-85db-5eaa4356c3fe.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk4MTkwODQsIm5iZiI6MTcwOTgxODc4NCwicGF0aCI6Ii8xNTEzOTU1MzUvMzEwODk3OTc3LTIyZTU1Yjc4LTQzNDUtNGZmNC04NWRiLTVlYWE0MzU2YzNmZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwN1QxMzM5NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MGIxZTQyNzBiMTAyZTU3ZGEyMzk2MTJjZDVlMTgzNDhhYTM0MjU2MTBlNjQzOGJmNjk2MTgxNmJjZTRkMGI2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Y8qPMHsfYaaXwAVq6sTIMK7YuHVgGxgXlhLdxst2gSA)
  
--------------------------------------------------------------------------------------
After adding tasks, you will be able to view all tasks and if necessary, assign another users task to yourself.
If no other users are added in the program, you will have to create a new user and a task.

![img](https://private-user-images.githubusercontent.com/151395535/310897982-e8f9c088-678a-4bb2-976d-87ed7b02e338.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk4MTkwODQsIm5iZiI6MTcwOTgxODc4NCwicGF0aCI6Ii8xNTEzOTU1MzUvMzEwODk3OTgyLWU4ZjljMDg4LTY3OGEtNGJiMi05NzZkLTg3ZWQ3YjAyZTMzOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwN1QxMzM5NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jMmFiOTk4Y2RhYzUwNjhiODU0ZjllYzE5YWMzMDNmZTQ0ZTA4ZmM3YTlkMWJiYzg0YjJjODBhOWY0NWJlZWUxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.1rKD3ZO483VBiXghvI7ejsEHLl7nh3PfQ9Wh9MCC5tc)

--------------------------------------------------------------------------------------
After creating a new user you can create new tasks for that user.

![img](https://private-user-images.githubusercontent.com/151395535/310897984-c50e8acd-c1a0-4a2e-add6-c2b146ee67c0.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk4MTkwODQsIm5iZiI6MTcwOTgxODc4NCwicGF0aCI6Ii8xNTEzOTU1MzUvMzEwODk3OTg0LWM1MGU4YWNkLWMxYTAtNGEyZS1hZGQ2LWMyYjE0NmVlNjdjMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwN1QxMzM5NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xNmRiYTQ2MTM1ZTc2OGY0MWJkOWYzM2UxMjFkN2FjNWM4NTAzMzEzZDc3YzlhOWQxOTNkZWZmMWQ0YzVlMTQ4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.XWAMMe2y0S68cS4Cl7TAiTB3z4BSI6FaQGYUD1Qd1cw) 

--------------------------------------------------------------------------------------
Once other users and tasks have been added you can then assign their tasks to yourself.

![img](https://private-user-images.githubusercontent.com/151395535/310897987-cce0aaea-7041-4b6f-b7f5-e42757a25234.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk4MTkwODQsIm5iZiI6MTcwOTgxODc4NCwicGF0aCI6Ii8xNTEzOTU1MzUvMzEwODk3OTg3LWNjZTBhYWVhLTcwNDEtNGI2Zi1iN2Y1LWU0Mjc1N2EyNTIzNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwN1QxMzM5NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MjVjZmViYjllNjE2ODc3ZDI1ZTI2ODgxMzhjOWE1ODg3OTIxNDY0MDkyMmJiYWQ0OGQ2ZGRiNGNmZGIzYjIyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.bl8cJVm3fzy608tIptFHMLAa1Vnl4R-5TBHJiVqvLuo) 

--------------------------------------------------------------------------------------
You can edit your own tasks. Once picking one of your tasks you can assign it to another user, edit the due date, mark as complete, or return to either of the menus.

![img](https://private-user-images.githubusercontent.com/151395535/310897991-53b05799-5fd3-4b06-8672-154dda91cafa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk4MTkwODQsIm5iZiI6MTcwOTgxODc4NCwicGF0aCI6Ii8xNTEzOTU1MzUvMzEwODk3OTkxLTUzYjA1Nzk5LTVmZDMtNGIwNi04NjcyLTE1NGRkYTkxY2FmYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwN1QxMzM5NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MWY4MDRmZTAyNDQ1MTE0MWU4M2ZmNTE2ZDU0ZmIxOGM0ZDY4ODNhODg4NTExMmFjY2NhNTlkNzk0NWI1MGYyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Eg8Hr43P-LmRIoHU0WDLMRcqzMWzhgJcgVvTAtbqf4U) 

--------------------------------------------------------------------------------------
You can generate a report to which will show task and user data.

![img](https://private-user-images.githubusercontent.com/151395535/310897994-94e3c5be-e7de-4469-9921-7b519d45d495.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk4MTkwODQsIm5iZiI6MTcwOTgxODc4NCwicGF0aCI6Ii8xNTEzOTU1MzUvMzEwODk3OTk0LTk0ZTNjNWJlLWU3ZGUtNDQ2OS05OTIxLTdiNTE5ZDQ1ZDQ5NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwN1QxMzM5NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yMWFiNjM0MmExMjMwNzc5NGYyMDcxYTFiYWFiMmQ1YjgzOTU0ZjliMmQzNTM1NjY4YzRhNTI3ZTdiMWM4OWI2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.tXZ7rU1697BiQ8J8ZX-vyfR--y06tQzmyzFaemNbbRI) 

--------------------------------------------------------------------------------------
You can view the report data in the terminal by displaying statistics

![img](https://private-user-images.githubusercontent.com/151395535/310897997-9486b47a-e69c-4964-bcae-fc1894a820f4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk4MTkwODQsIm5iZiI6MTcwOTgxODc4NCwicGF0aCI6Ii8xNTEzOTU1MzUvMzEwODk3OTk3LTk0ODZiNDdhLWU2OWMtNDk2NC1iY2FlLWZjMTg5NGE4MjBmNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwN1QxMzM5NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yYzNlMDY0MTJiMDY3ODU2ZDE4NWQ3ZTg0NGY3NWZiOTYyMDhlODczOGUwNTFkZjExYTRhMjJiNmRmMmNjMzMyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.z6ENtu1ZAujB_TKZ4xEdgQzSFNM6LNcaglfaKHrMZAg)

--------------------------------------------------------------------------------------
You can view the task overview text file if you wanted to print it out

![img](https://private-user-images.githubusercontent.com/151395535/310898000-88bfd358-b25d-40d7-b522-dd51eb554c69.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk4MTkwODQsIm5iZiI6MTcwOTgxODc4NCwicGF0aCI6Ii8xNTEzOTU1MzUvMzEwODk4MDAwLTg4YmZkMzU4LWIyNWQtNDBkNy1iNTIyLWRkNTFlYjU1NGM2OS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwN1QxMzM5NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MWIwNjMyODIwMzQ2NDQwMTU3ODA3NDhiNWE0MjJmNTE3OTMxOTNkZDFlM2U4NzNlNWQ3ZDgzYTFmNDU1M2RiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.TYzflUGOaNF7zFM3LZA8ux-60J-HFpWJ3uL9-Ob2gu8)

--------------------------------------------------------------------------------------
You can view the user overview text file if you wanted to print it out

![img](https://private-user-images.githubusercontent.com/151395535/310898002-48c32108-7797-403a-ba5f-bf442570ab6a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk4MTkwODQsIm5iZiI6MTcwOTgxODc4NCwicGF0aCI6Ii8xNTEzOTU1MzUvMzEwODk4MDAyLTQ4YzMyMTA4LTc3OTctNDAzYS1iYTVmLWJmNDQyNTcwYWI2YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwN1QxMzM5NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NmYwNjBlYWYwNGQwN2U5OTU0NmM1YTY2ZDQzN2JiODMwMGFiZTc2NDllNjE3Zjk5YzFiODAxZTczYWI3OGJjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9._CGgFEoNcPBa-BYiD_5TW5pynjmRA9ijPqm4X2gMsng)

--------------------------------------------------------------------------------------



(3.0)--------------------------------Original Code------------------------------------


#=====importing libraries===========

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


#Create tasks.txt if it doesn't exist

if not os.path.exists("tasks.txt"):

    with open("tasks.txt", "w") as default_file:

        pass

with open("tasks.txt", 'r') as task_file:

    task_data = task_file.read().split("\n")

    task_data = [t for t in task_data if t != ""]


task_list = []

for t_str in task_data:

    curr_t = {}

    # Split by semicolon and manually add each component

    task_components = t_str.split(";")

    curr_t['username'] = task_components[0]

    curr_t['title'] = task_components[1]

    curr_t['description'] = task_components[2]

    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)

    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)

    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====

'''This code reads usernames and password from the user.txt file to 

    allow a user to login.
'''

#If no user.txt file, write one with a default account

if not os.path.exists("user.txt"):

    with open("user.txt", "w") as default_file:

        default_file.write("admin;password")

#Read in user_data

with open("user.txt", 'r') as user_file:

    user_data = user_file.read().split("\n")

#Convert to a dictionary

username_password = {}

for user in user_data:

    username, password = user.split(';')

    username_password[ 'username'] = password

logged_in = False

while not logged_in:

    print("LOGIN")

    curr_user = input("Username: ")

    curr_pass = input("Password: ")

    if curr_user not in username_password.keys():

        print("User does not exist")

        continue

    elif username_password[curr_user] != curr_pass:

        print("Wrong password")

        continue

    else:

        print("Login Successful!")

        logged_in = True


while True:

    # presenting the menu to the user and 

    # making sure that the user input is converted to lower case.

    print()

    menu = input('''Select one of the following Options below:
    
r - Registering a user

a - Adding a task

va - View all tasks

vm - View my task

ds - Display statistics

e - Exit

: ''').lower()

    if menu == 'r':
        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        new_username = input("New Username: ")

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
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
        print("Task successfully added.")


    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            


    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        for t in task_list:
            if t['username'] == curr_user:
                disp_str = f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)
                
    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

(4.0)--------------------------------------Credits------------------------------------

Original Code Author: Hyperion Dev
Refactored Code Author: Stacy Parker