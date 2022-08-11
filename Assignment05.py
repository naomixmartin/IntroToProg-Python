# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <naomimartin>,<08.10.2022>, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None   # naomimartin: empty file handle
strFile = "/Users/naomimartin/Documents/Python_Foundations/Assignments/Assignment05/ToDoList.txt"   # An object that represents a file. naomimartin: specify full path for my own knowledge.
strData = ""   # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstRow = []    # naomimartin: A list that acts as a row
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
taskChoice = ""    # naomimartin: capture user input for "task" in step 4
priorityChoice = ""    #naomimartin: capture user input for "priority" in step 4
removeChoice = ""    #naomimartin: capture user input for "remove" option in step 5
saveChoice = ""    #naomimartin: capture user input for "save" option in step 6


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# naomimartin: first, write dictionary data into the .txt file.
objFile = open(strFile, "w")
dicRow = {"Task":"Grocery shopping", "Priority":"High"}
objFile.write(dicRow["Task"] + ", " + dicRow["Priority"] +"\n")
dicRow = {"Task":"Laundry","Priority":"High"}
objFile.write(dicRow["Task"] + ", " + dicRow["Priority"] +"\n")
dicRow = {"Task":"Work out","Priority":"Medium"}
objFile.write(dicRow["Task"] + ", " + dicRow["Priority"] +"\n")
objFile.close() # naomimartin: close connection to file. Best practices.

# naomimartin: next, load each row into a dictionary, then append these dictionaries into a list. List of dictionary rows.
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(", ") # naomimartin: returns a list. I specified that each task and priority must be split by ", " rather than "," so I have put that argument in here.
    dicRow={"Task":lstRow[0],"Priority":lstRow[1].strip()}
    lstTable.append(dicRow)

objFile.close()  # naomimartin: close connection to file. Best practices.
#print(lstTable) # naomimartin: to confirm the above worked.


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("1) Show current data\n")
        for row in lstTable:
            print("Task: " + row["Task"] + "; Priority: " + row["Priority"]) #naomimartin: shows the user each element of the list of dictionaries.
        input("\nPress the enter key to return to the menu. \n")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("2) Add a new item\n")
        taskChoice = input("Enter a task: ")
        priorityChoice = input("Enter your task's priority level: ")
        dicRow = {"Task": taskChoice.title(), "Priority": priorityChoice.title()}
        lstTable.append(dicRow)
        print("\nUser input recorded. Ensure that you select '4) Save Data to File' in the Menu of Options in order to update your To-Do List.") # naomimartin: reminder for user
        input("\nPress the enter key to return to the menu. \n")

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("3) Remove an existing item \n")
        i=1
        for row in lstTable:
            print(str(i) + ". Task: " + row["Task"] + "; Priority: " + row["Priority"])
            i += 1
        removeChoice = int(input("\nWhich item would you like to remove? "))
        if removeChoice < len(lstTable): #naomimartin: to ensure that the user selects a valid option within index range.
            del lstTable[removeChoice-1] # naomimartin: subtract 1 since indices start at 0 in Python.
            print("Task #" + str(removeChoice) + " has been removed.")
        else: #naomimartin: if user does not select a valid option within index range, print the message below.
            print("Please select a valid number to remove its row of data. ")
        input("\nPress the enter key to return to the menu. \n")

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("4) Save Data to File \n")
        saveChoice = input("Would you like to save your input to your To-Do list? (y)es or (n)o: ")
        if saveChoice == "y":
            objFile = open(strFile, "w")
            for row in lstTable:
                dicRow = {"Task": row["Task"], "Priority": row["Priority"]}  #naomimartin: Each row in the list is a dictionary; get dictionary values by specifying its key.
                objFile.write(dicRow["Task"] + ", " + dicRow["Priority"] + "\n")
            print("User input saved.")
            objFile.close()  # naomimartin: close connection to file. Best practices.
        elif saveChoice == "n":
            print("User input not saved.")
        input("\nPress the enter key to return to the menu. \n")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program

    else:
        print("Invalid menu option. Please select a valid option [1 to 5] - ") # naomimartin: added so that if anything other than the menu options are selected, inform the user that a valid menu option must be selected
        continue