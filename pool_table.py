from datetime import datetime
from title_screen import title_screen
import json

file_object = open("tables.txt", "w")


pool_tables = []


title_screen()

def show_tables():
    for pool_table in pool_tables:
        print(f"Table {pool_table}")

# options_menu()

class PoolTable:
    def __init__(self, table_no):
        self.table_no = table_no
        self.is_available = "Open"
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        #start start
        #end time

    def __repr__(self):
        return (f"{self.table_no} is {self.is_available}")

    def check_out(self):
        now = datetime.now()
        self.is_available = now.strftime("Occupied %b %d, %y || %H:%m:%S")
        #self.start_time =
        self.end_time = datetime.now()


    def check_in(self):
        now = datetime.now()
        self.is_available = "Open"
        self.end_time = now




for i in range(1,13):
    pool_table = PoolTable(i)
    pool_tables.append(pool_table)


def table_selection():
    user_input = ""
    while user_input != 0:
        show_tables()
        user_input = int(input("""
Please select a table:
"""))
        table_choice = user_input - 1
        pool_table = pool_tables[table_choice]
        pool_table.check_out()
        break
        options_menu()


def return_table():
    user_input = int(input("""
Which table would you like to check in:
"""))
    while user_input != 0:
        table_choice = user_input - 1
        pool_table = pool_tables[table_choice]
        pool_table.check_in()
        break

# def options_menu():
#     print("""
# OPTIONS
# Please select one of the following:
# R) to rent out a table
# C) to check a table back in
# V) to view tables
# Q) to quit to title screen
# """)

# options_menu()

user_input = ""
while user_input != "q":
    user_input = input("""
                                  OPTIONS MENU

                        Please select one of the following:
                        -----------------------------------
                        R) to rent out a table
                        C) to check a table back in
                        V) to view tables
                        Q) to quit to title screen
                        -----------------------------------
""")
    if user_input == "r":
        table_selection()
    elif user_input == "c":
        return_table()
    elif user_input == "v":
        show_tables()
    elif user_input == "q":
        title_screen()


        def return_table():
            user_input = int(input("""
        Which table would you like to check in:
        """))
            table_choice = user_input - 1
            pool_table = pool_tables[table_choice]
            pool_table.check_in()
