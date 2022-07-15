import tkinter.ttk
from tkinter import *
import csv
from data_warehouse import create_user, remove_user


# TODO
# 1. Loging into users page
# 2. Problem with username's having special characters and spaces
# 4. README file


# create list of user usernames from file user_names.csv and return it as a list
def get_names():
    with open('users\\user_names.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', lineterminator='\n')

        all_users = []
        for v in csv_reader:
            all_users.append(v)
        return all_users


#
# Function creates window and asks user if he wants to delete user with given name.
def sure_delete(username):
    wd = Tk()
    wd.title('Expense Tracker')
    wd.geometry("290x250")

    Label(wd, text=f"Are you sure you want to delete user {username}?").grid(columnspan=3, column=0, row=0)
    Button(wd, text="Yes", command=lambda: x(username, wd)).grid(column=0, row=1)
    Button(wd, text="No", command=lambda: wd.destroy()).grid(column=2, row=1)


def x(username, dd):
    remove_record(username)
    dd.destroy()


#
# refresh user_box treeview (after deleting or adding new user)
def refresh_names(tree):
    # delete
    tree.delete(*tree.get_children())
    names = get_names()
    xt = 1
    for v in names:
        tree.insert(parent='', index='end', text='', values=(i, v))
        xt += 1


#
# use data_warehouse function create_user to create new user with name given in new_username Entry
def remove_record(name):
    # use function to delete user's files and his name from user_names.csv file
    remove_user(name)
    # refresh user_box treeview
    refresh_names(user_box)


#
#
def add_record(name):
    # use function to create user's folder and file and add his name to user_names.csv file
    create_user(name)
    # refresh user_box treeview
    refresh_names(user_box)


#
# Create window
root = Tk()
root.title('Expense Tracker')
root.geometry("290x500")

#
# create treeview containing all users from file user_names.csv
# user_treeview()
user_box = tkinter.ttk.Treeview()

user_box['columns'] = ['ID', 'Name']

user_box.column('#0', width=0, stretch=NO)
user_box.column('ID', width=40, anchor=W)
user_box.column('Name', width=250)

user_box.heading('#0', text='')
user_box.heading('ID', text='ID')
user_box.heading('Name', text='Name')

data = get_names()

i = 1
for value in data:
    user_box.insert(parent='', index='end', text='', values=(i, value))
    i += 1
user_box.grid(column=0, row=0, columnspan=2, sticky=NS)

# removing user # remove_user(user_box.item(user_box.focus(), 'values')[1])
Button(root, height=1, width=15, text="Remove User",
       command=lambda: sure_delete(user_box.item(user_box.focus(), 'values')[1])).grid(padx=10, pady=5, column=0,
                                                                                       row=1, columnspan=2)

#
# Create Button, Label and Entry used for creating new user.
# Clicking Button runs the data_warehouse.py function create_user(). Program gives string value written to
# "new_username" Entry to function create_user(). #create_user(new_username.get())
Button(root, height=2, width=19, text="Add User", command=lambda: add_record(new_username.get())).grid(padx=2, pady=5,
                                                                                                       column=1, row=2,
                                                                                                       rowspan=2,
                                                                                                       sticky=W)
Label(root, text="New User Username").grid(column=0, row=2)
new_username = tkinter.ttk.Entry(root)
new_username.grid(column=0, row=3)
# logging
Button(root, height=3, width=20, text="Open User's Tracker").grid(padx=10, pady=5, column=0, row=4, columnspan=2)

refresh_names(user_box)
# close window
root.mainloop()
