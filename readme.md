# Login System

## About

*A Login System Made with Python 3.9*

It supports functionality like creating an account, logging in, changing the password of an account and deleting an account. The passwords are encrypted so access to the username-password index wouldn't let an hacker know the password to your account. 

> The program only supports the following characters:
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#!@$%^&*()[] <>?/;:`~,.'"=_

---
## How it Works:
   

- ### Overview :
   * The main.pyw file shows four buttons of the four features(Signing up, Logging in, deleting, changing password), each feature has two files, one for the front end and one for the backend. 
   
   * Some files checks.py, hashing.py, backEndUtilityFuncs.py and the guiUtilityFuncs.py are files that either stop repetetive code or have seperate logic.


- ### Individual file list :
   
   * **main.pyw** - Main execution of the program, shows all the features.
   
   * **deleteAccountGui.py** - Front End of the deleting account feature.

   * **deleteAccount.py** - Back End of the deleting account feature.

   * **loginGui.py** - Front End of the Log In feature.

   * **login.py** - Back End of the Log In feature.

   * **passChangeGui.py** - Front End of the password change feature.

   * **passChange.py** - Back End of the password change feature.

   * **signUpGui.py** - Front End of the creating account feature.

   * **signUp.py** - Back End of the creating account feature.

   * **checks.py** - Checks a given username and password combination, assuring all rules are followed.

   * **guiUtilityFuncs.py** - Functions that are used by the front end files.
   
   * **backEndUtilityFuncs.py** - Functions that are used by the back end files.

   * **hashing.py** - Hashes a given string(for encrypting passwords)
   

- ### Interaction between files :
   * The main.pyw file uses the deleteAccountGui.py, loginGui.py, passChangeGui.py and signUpGui.py file according to the button clicked. 

   * The deleteAccountGui.py, loginGui.py, passChangeGui.py and signUpGui.py use the deleteAccount.py, login.py, passChange.py and signUp.py files respectively for the backend.

   * The gui files(deleteAccountGui.py, loginGui.py, passChangeGui.py, signUpGui.py) use the guiUtilityFuncs.py files to create the gui, as the guiUtilityFuncs.py contains the blue print and repetetive code needed by the files.

   * The deleteAccount.py removes the particular username-password combination from the data.txt file, the login.py checks the username-password combination in the data.txt file. The passChange.py file changes the password of a given username, signUp.py file makes and stores the username-password combination in the data.txt file. These backend files use the backEndUtilityFuncs.py file for repetetive tasks.

   * For all the reading and writing from the data.txt to take place the passwords need to be encrypted. The hashing.py takes in a string and encrypts it.

   * While creating an account or changing password, the checks.py file does important checks, like the strength of the password, checking if no duplicate accounts can be made etc.  


<br><br>

*-Thank you* 
