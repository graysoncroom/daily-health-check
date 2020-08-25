# daily-health-check
A simple python script made in an attempt to automate an annoying daily COVID-19 survey.

## Dependencies
This script uses a library called splinter to run and manage a browser (typically headless) via python.

To install splinter, make sure you have pip and run: `pip install splinter`

Note that this may require admin level privileges as it installs the library globally.

## Required Data Files

In the same directory as the script, you must have the following two files:

1) utd_email_and_pass.txt

    * your email should be written on the first line
    * your password should be written on the second line
    * do not put additional lines or spaces in this file
    * comments are not respected in this file

2) authentication_codes.txt
    * authentication codes should be newline seperated with no whitespace
    * codes that are used will be commented out with a # and a space at the
      beginning of the line
    * you can also put your own comments in this file by putting # and a space at
      the beginning of any line
      
      
 ## What is an authentication code?
 
 There are three ways the system can authenticate you, those being:
 
 1) Through Duo Security pushing a notification to your phone, which you either accept or decline.
 2) By calling your phone via an automated system and having you click a specific number.
 3) You can request a collection of 10 authentication codes to be sent to your phone via text message. 
    You then take note of this collection and use the codes once each time you want to log in to your email.
    
 Note that each code should be 7 digits long.
    
 ## How does this script use these auth codes?
 
 All you have to do is follow the rules stated above for the authentication_codes.txt file using the codes given to you.
 
 Note that you must obtain these codes manually and put them in that file to be used by the script.
