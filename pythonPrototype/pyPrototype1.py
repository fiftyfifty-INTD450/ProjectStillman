# Prototype 1 
# 1. untitled title
# 2. enter your name, birthday, email
# 3. terms and condition; super long. yes or no.
# 	3.1 if they say no, keep asking until they say yes. 
# 	3.2 if they say yes, print out a smiley face then clear screen
# 		Welcome. The session will begin in 3, 2, 1... 
# 			Opens up windows GUI


# Prototype 2 
# 1. untitled title
# 2. enter your name, birthday, email
# 3. terms and condition; super long. yes or no.
# 	3.1 if they say no, keep asking until they say yes. 
# 	3.2 if they say yes, print out a smiley face then clear screen
# 		Welcome. The session will begin in 3, 2, 1... 

import time, sys, os
import smtplib
from email.mime.text import MIMEText

def main():
    begin()

def begin():
    # GAME TITLE
    # TODO: Slow down the printing.
    print('''
        ####     ####                     ###          ##         ###           #####                           ####
        ####     ####                     ###          ##         ###              ##                             ##   
        ####     ####                     ###                     ###              ##        ######               ##
        ####     ####   ###########    ############   ####     ############        ##     ###      ###       #######       
        ####     ####   #############     ###           ##        ###              ##     ############     ##     ##
        ####     ####   ####     ####     ###           ##        ###              ##     ###             ###     ##
         ###########    ####     ####     ###   ###     ##        ###   ###        ##     ###      ###    ###     ##
           #######      ####     ####        ###      ######         ###        ########     ######         ######  ##       
                                                                                                                          
    ''')
    for i in range(101):
        if (i == 100):
            # When it reaches 100, print on new line.
            print('Loading [%d%%]\r'%i)
            time.sleep(0.5)
            print("Done.")
            time.sleep(0.5)
            print("Booting server...")
            time.sleep(0.5)
        else: 
            time.sleep(0.1)
            print('Loading [%d%%]\r'%i, end="")

    # REQUEST USER INFO
    # TODO: Filter input.
    username = input("Please type in your full name: ")
    bday = input("Please type in your birthday: ")
    email = input("Please type in your e-mail: ")

    # Print terms and conditions
    with open("terms.txt", "r") as terms: 
        print(terms.read()*3)

    # Force user to agree to terms and conditions
    agree = False
    while not agree:
        userAgrees = input("Do you agree to the terms and conditions? [Y/N]: ")
        if (userAgrees[0].lower() == "y"):
            agree = True
    print("Thank you.")
    time.sleep(0.8)
    os.system('clear')
    time.sleep(0.5)
    print("Sending e-mail...")
    time.sleep(0.8)
    print("Email sent. Please check your inbox.")
    time.sleep(0.8)

    # TODO: SEND E-MAIL

main()