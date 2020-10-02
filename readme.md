This is a login system made with Python 3

    How it Works:
   
       It has an image,data.txt, hashing.py, login.py, login_gui.py, main.py, signup.py, sign_up_gui.py, checks.py files.

      The image is displayed on the front, when the user clicks on the login button the login_gui file is called and when the user clicks on the sign up button the sign up file is called.

      The sign_up_gui file shows two input boxes, one to enter the username and one to enter the password, then it uses the signup file to actually creat an account.

      The login_gui file shows the input boxes, one to enter the username and one to enter the password, then it uses the login file to check if the combination is correct.

      The login file takes the username and password, it searches through the text file(data.txt), when it finds the match, it takes the corresponding password and then hashes the password given, if the passwords match it return True.

      The signup file takes the username and password, check the username and password, hash the password and then store the combination in the text file(data.txt).

      The hashing file takes a string and then hashes the password using an algorithm that is not very good but is made by me, good enough for the purposes of this login system

      The checks.py file performs some checks which can to see the sign up is done securely and perfectly following all the rules.
      
    That's it!
  
  
  
You can take this code and change the photo if you want. Unfortunately I can't gurantee if it would work on every system. I am constantly improving this project
open to any suggestions.
  
