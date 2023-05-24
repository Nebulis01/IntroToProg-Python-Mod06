# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Nathan Shelby,09MAY2023,Added code to complete assignment 5
# Nathan Shelby,23MAY2023,Added code to complete assignment 6
# ------------------------------------------------------------------------ #

# -- Import -- #
import os  # Import module for file system operations

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection

# using lstTable as global variable so that multiple functions can utilize it


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
def filework():
    global lstTable
    if os.path.isfile(objFile):
        importfile = open(objFile, "r")
        skipfileline = importfile.readlines()[1:]
        for row in skipfileline:
            lstRow = row.split(",")
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
            lstTable.append(dicRow)
            importfile.close()
        return lstTable

    else:
        importfile = open(objFile, "w")
        lstRow = ["Task", "Priority"]
        importfile.write(lstRow[0] + "," + lstRow[1] + "\n")
        lstRow = ["Vacuum Carpet", "1"]
        importfile.write(lstRow[0]+","+lstRow[1]+"\n")
        lstRow = ["Wash Windows", "2"]
        importfile.write(lstRow[0] + "," + lstRow[1] + "\n")
        lstRow = ["Clean Dishes", "3"]
        importfile.write(lstRow[0] + "," + lstRow[1] + "\n")
        importfile.close()
        importfile = open(objFile, "r")
        skipfileline = importfile.readlines()[1:]
        for row in skipfileline:
            lstRow = row.split(",")
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
            lstTable.append(dicRow)
        importfile.close()
        return lstTable

def selection1():
    print("This the current To Do List:")
    for objrow in lstTable:
        print(objrow)

def selection2():
    strTask = input("Enter Task Name:")
    strPriority = input("Enter Priority:")
    dicRow = {"Task": strTask, "Priority": strPriority}
    lstTable.append(dicRow)
    for objrow in lstTable:
        print(objrow)
def selection3():
    print("You will need to review the list and enter the index value for removal:")
    print("The index values are:")
    for objrow in range(len(lstTable)):
        print(objrow, end=" ")
        print(lstTable[objrow])
    strIDRemove = int(input("Enter an ID to Remove:"))
    del lstTable[strIDRemove]

def selection4():
    for objrow in lstTable:
        print(objrow)
    print("Saving above list to file")
    writefile = open(objFile, "w")
    lstRow = ["Task", "Priority"]
    writefile.write(lstRow[0] + "," + lstRow[1] + "\n")
    for objrow in lstTable:
        strtowrite = objrow['Task'] + "," + objrow['Priority'] + "\n"
        writefile.writelines(strtowrite)
    writefile.close()
    print("Successfully saved to file.")
def selection5():
    print("Goodbye")
    exit()  # Exit the program

filework()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        selection1()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        selection2()
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        selection3()
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        selection4()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        selection5()