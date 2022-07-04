import os
import csv


# Function create_user() only takes string variable user_name
# if said username was already in use function returns FALSE
# if it's not function follows these directions, and then returns TRUE.
#
# function creates new folder (with necessary files in it)
# in path: //expense_tracker//users named after new user username
# then adds this user username to user_names.csv file
#
# user folder named "user_nickname" contains:
# file "user_nickname_category.csv" containing all categories (customary and normal ones)
# file "user_nickname_table.csv" contains all records given by user
# file "user_nickname_backup_table.csv" is a backup file of "user_nickname_table.csv" data
#
def create_user(username):

    # check if username is already in file user_names.csv
    with open('users\\user_names.csv', 'r') as f:
        x = csv.reader(f, delimiter=',', lineterminator='\n')
        # go through all lines and check each one of them if there is already user username there
        # if it is, then return FALSE
        for lines in x:
            if username in lines[0]:
                return False

    # write down user nickname in user_names.csv
    with open('users\\user_names.csv', 'a') as f:
        csv_writer = csv.writer(f, delimiter=',', lineterminator='\n')
        csv_writer.writerow([username])

    #
    # create folder named "user_nickname"
    os.makedirs("users\\"+username)

    # create file "user_nickname_category.csv" in folder "username"
    # dodaj kategorie jak (jedzenie, rozrywka)
    with open(f'users\\{username}\\{username}_category.csv', "w") as file:
        # categories is a list of categories of expanses
        categories = ['food', 'fitness']
        csv_writer = csv.writer(file, delimiter=',', lineterminator='\n')
    # create file "user_nickname_table.csv"
    with open(f'users\\{username}\\{username}_table.csv', "w") as file:
        pass
    # create file "user_nickname_backup_table.csv"
    with open(f'users\\{username}\\{username}_backup_table.csv', "w") as file:
        pass

    # return TRUE and end function
    return True


# Function remove_user() takes string value of user username that is to be removed, **
# to avoid mistakes if user is already deleted function returns FALSE,
# if not it follows deletes user files and returns True.
#
# Function deletes user username from file user_names.csv and this user folder along with all files.
#
def remove_user(username):

    # check if user is in file user_names.csv
    with open('users\\user_names.csv', 'r') as f:
        x = csv.reader(f, delimiter=',', lineterminator='\n')
        # go through all lines and check each one of them if there is already user username there
        # if it is not, then return FALSE
        for lines in x:
            if username not in lines[0]:
                return False

    # delete user username from



# Function add_record() takes:
# date (datetime**) - date of expanse,
# type (string) - type of expanse,
# amount (float) - amount of money for expanse,
# currency (string) - currency of money paid for expanse,
# name (string) - name of expanse,
# quantity (string) - quantity.
#
# Function adds new record to user file "user_nickname_table.csv" with said data and additional id.
#
def add_record():
    pass


# Function remove_record() takes id of record that is to be removed.
# Function deletes record with given id in file "user_nickname_table.csv".
def remove_record():
    pass


# Function alter_record() takes id int variable that is to be altered.
# Function changes record with given id.
#
def alter_record():
    pass


# Function add_expense_type() takes expense_type (string) variable that is to be added.
#
# Function firstly checks if expense_type variable is already in file "user_nickname_category.csv",
# if so it returns FALSE. If it's not then it adds expense_type variable to it, and returns TRUE.
#
def add_expense_type(expense_type):
    pass


# Function remove_expense_type() takes expense_type (string) variable that is to be removed.
#
# Function firstly checks if expense_type variable is in file "user_nickname_category.csv",
# if it's not it returns FALSE. If it's then it deletes matching value, then returns TRUE.
#
def remove_expense_type(expense_type):
    pass


# Function alter_expense_type() takes expense_type, new_expense_type (string) variables that is to be altered.
#
# Function firstly checks if expense_type variable is in file "user_nickname_category.csv",
# if it's not it returns FALSE. If it's then it deletes matching value, and adds new_expense_type variable,
# then it returns TRUE.
#
def alter_expense_type(expense_type, new_expense_type):
    pass
