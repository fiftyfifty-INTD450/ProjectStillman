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

import time, sys
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
    time.sleep(0.5)
    print("Sending e-mail...")
    time.sleep(0.8)
    print("Email sent. Please check your inbox")

    # SEND E-MAIL
    #textfile = open("msg.txt", 'r')
    with open("msg.txt", 'r') as emailMsg:
        msg = MIMEText(emailMsg.read())

    msg['Subject'] = 'Welcome!'
    msg['From'] = "friend@untitled.com"
    msg['To'] = email

    s = smtplib.SMTP('localhost', 1025)
    s.sendemail("friend@untitled.com", [email], msg.as_string())
    s.quit()

main()