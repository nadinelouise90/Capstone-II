import datetime

GREEN = "\033[92m"
LIGHTRED = "\033[91m"
WHITE = "\033[0m"
CYAN = "\033[96m"

password_file = open("user.txt", "r")
task_file = open("tasks.txt", "r")

# Login Section
# The program reads usernames and passwords from the user.txt file
# If both the inputted username and password match the data in the user.txt file, the menu of options is displayed.
# If the user logs in as 'admin' a specific menu is displayed.
# A while loop is used to repeatedly ask the user for their username and password until there is a match.

print("═════════════ Task Management System ══════════════")
print("                 PLEASE LOG IN                     ")
print("═══════════════════════════════════════════════════")

user_data = password_file.readlines()

while True:
    entered_username = input("\nWhat is your username? ")
    entered_password = input("What is your password? ")
    admin = False
    for line in user_data:
        login_pair = line.split(", ")
        username = login_pair[0]
        password = login_pair[1].strip("\n")
        if entered_password == password and entered_username == username and entered_username == "admin":
            print(f"{GREEN}Login Successful!")
            admin = True
        elif entered_password == password and entered_username == username and entered_username != "admin":
            print(f"{GREEN}Login Successful!")
            admin = False
        else:
            continue

        # Menu Option (admin)
        while True:
            if admin == True:
                print(
                    f"\n{CYAN}═════════════════════MENU═════════════════════════{WHITE}")
                menu = input('''Select one of the following options below:
💠 r  - Register a user
💠 a  - Add a task
💠 va - View all tasks
💠 vm - View my tasks
💠 s  - Display statistics
💠 e  - Exit
══════════════════════════════════════════════════
: ''').lower()
            # Menu Option (all other users)
            elif admin == False:
                print(
                    f"\n{CYAN}═════════════════════MENU═════════════════════════{WHITE}")
                menu = input('''Select one of the following options below:
💠 r  - Register a user
💠 a  - Add a task
💠 va - View all tasks
💠 vm - View my tasks
💠 e  - Exit
══════════════════════════════════════════════════
: ''').lower()

            # Registering a new user.
            # The user is prompted to input a new username and password but only if the user has logged in as 'admin'.
            # If any other user elects this menu option, an error message is displayed and the menu is shown again.
            # Once password is confirmed, the username and password is written to the user.txt file on a new line.
            if menu == "r" and entered_username == "admin":
                with open("user.txt", "a") as file:
                    print(
                        "To register a new user we will require the following information:\n")
                    new_username = input("What is the username? ")
                    new_password = input("What is the password? ")
                    new_password_confirm = input(
                        "Please confirm the password: ")
                    if new_password == new_password_confirm:
                        print(f"{GREEN}Success: User now registered!{WHITE}\n")
                        file.write(f"{new_username}, {new_password}\n")
                    else:
                        print(
                            f"{LIGHTRED}Your passwords do not match. Please try again.{WHITE}\n")

            # Adding a new task.
            # The user is prompted to input information about a new task.
            # This information is written to the tasks.txt file together with the current date.
            elif menu == "a":
                with open("tasks.txt", "a") as file:
                    now = datetime.datetime.now()
                    current_time = now.strftime("%d %b %Y")
                    print(
                        "To add a new task we will require the following information:\n")
                    user_name = input(
                        "What is the username of the person to whom the task is assigned? ")
                    title = input("What is the title of the task? ")
                    description = input("What is the task description? ")
                    due_date = input("What is the task due date? ")
                    file.write(
                        f"{user_name}, {title}, {description}, {current_time}, {due_date}, No\n")
                    print(f"{GREEN}Success: New task added! {WHITE}\n")

            # View all tasks.
            # When elected, the program will print all tasks from the tasks.txt file to the console in a reader friendly manner.
            elif menu == "va":
                with open("tasks.txt", "r") as file:
                    data = file.readlines()
                    for count, line in enumerate(data, start=1):
                        split_data = line.split(", ")
                        print(
                            f"╔═══════════════════════════════════════════════ Task {count} ══════════════════════════════════════════════════════════╗")
                        print(f"    Task:\t\t{split_data[1]}")
                        print(f"    Assigned to:\t{split_data[0]}")
                        print(f"    Date Assigned:\t{split_data[3]}")
                        print(f"    Due Date:\t\t{split_data[4]}")
                        print(f"    Task Complete?\t{split_data[5]}")
                        print(f"    Task Description:\n    {split_data[2]}")
                        print(
                            "╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\n\n")

            # View tasks assigned to specific user.
            # The program will check whether the username exists in the tasks.txt file and will print out the task specifics.
            elif menu == "vm":
                with open("tasks.txt", "r") as file:
                    data = file.readlines()
                    user_names = [line.split(", ")[0] for line in data]
                    if entered_username in user_names:
                        for line in data:
                            split_data = line.split(", ")
                            if entered_username == split_data[0]:
                                print(
                                    f"╔═══════════════════════════════════════════════ {entered_username} ══════════════════════════════════════════════════════════╗")
                                print(f"    Task:\t\t{split_data[1]}")
                                print(f"    Assigned to:\t{split_data[0]}")
                                print(f"    Date Assigned:\t{split_data[3]}")
                                print(f"    Due Date:\t\t{split_data[4]}")
                                print(f"    Task Complete?\t{split_data[5]}")
                                print(
                                    f"    Task Description:\n    {split_data[2]}")
                                print(
                                    "╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\n\n")
                    elif entered_username not in user_names:
                        print(
                            f"{LIGHTRED}The logged in user doesn't have tasks to display{WHITE}")

            # View statistics.
            # This option is only available on the menu displayed to the 'admin' user.
            # It counts the number of tasks and makes a list of unique users to capture the total.
            elif menu == "s" and entered_username == "admin":
                with open("tasks.txt", "r") as task_file, open("user.txt", "r") as user_file:
                    data = task_file.readlines()
                    user_data = user_file.readlines()
                    task_quantity = len(data)
                    user_names = []
                    unique_users = []
                    count = 0
                    for line in user_data:
                        split_data = line.split(", ")
                        user_names.append(split_data[0])
                    for user in user_names:
                        if user not in unique_users:
                            count += 1
                            unique_users.append(user)
                    print(
                        f"╔════════════════════════════════════ Statistics ═══════════════════════════════════════════╗")
                    print(f"\tNumber of Tasks:\t{task_quantity}")
                    print(f"\tNumber of unique users:\t{count}")
                    print(
                        "╚═══════════════════════════════════════════════════════════════════════════════════════════╝\n\n")

            # Exit the program and close the txt files.
            elif menu == "e":
                print("Goodbye!!!")
                password_file.close()
                task_file.close()
                exit()

            # These are the error messages displayed if the user enters the wrong selection or username/password.
            else:
                if menu == "r" and entered_username != "admin":
                    print(
                        f"{LIGHTRED}Only the admin is allowed to register users. Please choose another option or log in as admin.{WHITE}")
                else:
                    print(
                        f"{LIGHTRED}You have made a wrong choice! Please try again!{WHITE}")
    else:
        print(f"{LIGHTRED}Login Unsuccessful! Please try again!{WHITE}")
        continue
