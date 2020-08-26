# daily-health-check
A simple python script made in an attempt to automate an annoying daily COVID-19 survey.

It is not my intention to violate any UTD guidelines, nor am I aware if I am doing so. 
The only intention is to automate the process of completing the daily health check every day 
with a much higher accuracy brought forth by the automation.

I do not accept any responsibility for any other person other than myself utilizing this script.

I recommend that this script should be used for educational purposes only.

## Dependencies
This script uses a library called splinter to run and manage a browser (typically headless) via python.

This script also uses the chromedriver which you can find here: https://chromedriver.chromium.org/

To install splinter, make sure you have pip and run: `pip install splinter`

Note that this may require admin level privileges as it installs the library globally.

To install chromedriver, go to the link above and download the correct version for your system.

This will download a compressed file, extract the chromedriver.exe file and place it somewhere in your path.

## Program arguments

You must run this script with either, "Yes"/"yes" or "No"/"no" which correspond to answers of the question: 

Will you be on campus today?

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
 
 ## Issues/Bugs
 
 For whatever reason, the last authentication code is never able to be used. I need to figure out why at some point.
 
 ## Other Notes
 
 If you want the browser this script controls to run in headless mode, swap out `with Browser('chrome', headless=False) as browser:` for `with Browser('chrome', headless=True) as browser:`.
 
 I'll make this a script option at some point.
