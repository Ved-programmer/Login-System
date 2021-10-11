<!-- markdownlint-disable-file -->

# Login System

## About

*A Login System Made with Python*

It supports functionality like creating an account, logging in, changing the password of an account and deleting an account. The passwords are encrypted so access to the username-password index wouldn't let an hacker know the password to your account. 

> The program only supports the following characters:
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#!@$%^&*()[] <>?/;:`~,.'"=_

---
## How it Works:
   

- ### Overview :
   * The main.pyw is the main entry point to the program. 
   
   * The starting screen shows four buttons of the four features(Signing up, Logging in, Deleting, Changing password)

   

- ### Interaction between files :
   * The main.pyw file uses the deleteAccountGui.py, loginGui.py, passChangeGui.py and signUpGui.py file according to the button clicked. 

   * For all the reading and writing from the data.txt to take place the passwords need to be encrypted for security reasons. The hashing.py takes in a string and encrypts it.

   * While creating an account or changing password, the checks.py file does important checks, like the strength of the password, checking if no duplicate accounts can be made etc.  
