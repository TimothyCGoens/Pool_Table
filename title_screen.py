

eight_ball = """
|--------------------------------------------------------------------------|
|                                                                          |
|                                                                          |
|                                                                          |
|               ____                                                       |
|           ,dP9CGG88@b,                                                   |
|         ,IP  _   Y888@@b,          Pool Hall Systems                     |
|        dIi  (_)   G8888@b          ©1993 Tim Goens                       |
|       dCII  (_)   G8888@@b                                               |
|       GCCIi     ,GG8888@@@.                                              |
|       GGCCCCCCCGGG88888@@@..                                             |
|       GGGGCCCGGGG88888@@@@...                                            |
|       Y8GGGGGG8888888@@@@P....                                           |
|        Y88888888888@@@@@P.....                                           |
|        `Y8888888@@@@@@@P'.....                                           |
|           `@@@@@@@@@P'.......                                            |
|              '''''' ......                                               |
|                                                                          |
|                                    Press E to Enter                      |
|                                    Press Q to quit                       |
|                                                                          |
|                                                                          |
|--------------------------------------------------------------------------|"""


def title_screen():
    user_input = input(eight_ball)

user_input = ""

if user_input == "e":
    options_menu()
elif user_input == "q":
    print("Thank you for using Pool Hall Systems.")

import pool_table
