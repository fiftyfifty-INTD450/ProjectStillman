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

     # Depending on their maritial status, have a following question?
    maritial = input("Please indicate your maritial Status [married/single/widowed]: ")

    # Force user to agree to download the files
    agree = False
    while not agree:
        userAgrees = input("Update found. Do you want to download the files [Y/N]?: ")
        if (userAgrees[0].lower() == "y"):
            agree = True

    # Print a bunch of standard installation statements
    with open("terms.txt", "r") as terms: 
        updateMsg = terms.read()
    for line in updateMsg.splitlines():
        print(line)
        time.sleep(0.2)
    
    # Clear screen for thank you message
    time.sleep(0.5)
    os.system('clear')
    time.sleep(0.8)
    print("Thank you.")
    time.sleep(0.8)

    # Clear screen for e-mail sent message.
    os.system('clear')
    time.sleep(0.5)
    print("Update complete. E-mail confirmation was sent.")
    time.sleep(0.8)
    print("Please check your inbox.")
    time.sleep(0.8)

    # TODO: SEND E-MAIL

main()