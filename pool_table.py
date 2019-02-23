file_object = open("tables.txt", "w")


import time
import datetime
from datetime import date
from title_screen import title_screen
import json
localtime = time.asctime( time.localtime(time.time()) )



pool_tables = []

# calls title_screen function in another file
title_screen()

class PoolTable:
    def __init__(self, table_no):
        self.table_no = table_no
        self.is_available = "Open"
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        self.display_start_time = time.time()
        self.display_end_time = time.time()
        self.cost = 0

    def __repr__(self):
        return (f"""{self.table_no} is {self.is_available}""")

    def check_out(self):
        now = datetime.datetime.now()
        self.is_available = now.strftime("Occupied")
        self.start_time = now.strftime("%H:%m:%S")
        self.display_start_time = time.time()


    def check_in(self):
        now = datetime.datetime.now()
        self.is_available = "Open"
        self.end_time = now.strftime("%H:%m:%S")
        self.display_end_time = time.time()
        total_time = (self.display_end_time - self.display_start_time)/60
        self.cost = round(total_time * .50)
        self.total_time = round(total_time)

        with open("tables.txt", "a") as file_object:
            file_object.write(f"""
---------------------------------------
Table {self.table_no}
Start Time: {self.start_time}
End time: {self.end_time}
Total Time Played: {self.total_time}
Total ${self.cost}
---------------------------------------""")


# creates 12 pool tables and puts them into a list
for i in range(1,13):
    pool_table = PoolTable(i)
    pool_tables.append(pool_table)


def table_selection():
    try:
        user_input = ""
        while user_input != 0:
            show_tables()
            user_input = int(input("""\nPlease select a table: """))
            table_choice = user_input - 1
            pool_table = pool_tables[table_choice]
            if pool_table.is_available == "Occupied":
                print("""
------------ERROR-------------------------------------------------               
WHOOPS!  Table is already in use, let's check out a different one!
------------------------------------------------------------------""")
            else:
                pool_table.check_out()
            break
            options_menu()
    except ValueError:
        print("""\n
----------------ERROR------------------------------------
**DOH!  You have to choose the number of a table silly!**
---------------------------------------------------------""")


def return_table():
    try:
        show_tables()
        user_input = int(input("""\nWhich table would you like to check in: """))
        while user_input != 0:
            table_choice = user_input - 1
            pool_table = pool_tables[table_choice]
            if pool_table.is_available == "Open":
                print("""
------------ERROR---------------------------------------------
Yo! You can't check this one in, because it isn't checked out!
--------------------------------------------------------------""")
            else:
                pool_table.check_in()
            break
    except:
        print("""\n
----------------ERROR---------------------------
**OH NO!  What did you do, not enter a number?**
------------------------------------------------""")

def show_tables():
    for pool_table in pool_tables:
        print(f"Table {pool_table}")

user_input = ""
while user_input != "q":
    user_input = input("""\n
                                  OPTIONS MENU

                        -----------------------------------
                        R) to Rent a Table
                        C) to Check Table In
                        V) to View Tables
                        Q) to Quit to Title
                        -----------------------------------
                              Make your selection:
                                      """)

    if user_input == "r":
        table_selection()
    elif user_input == "c":
        return_table()
    elif user_input == "v":
        show_tables()
    elif user_input == "q":
        title_screen()
