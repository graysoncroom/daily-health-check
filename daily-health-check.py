#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from splinter import Browser
from time import sleep
import sys

# In this same directory you must have two files:
#    1) utd_email_and_pass.txt
#        * your email should be written on the first line
#        * your password should be written on the second line
#        * do not put additional lines or spaces in this file
#        * comments are not respected in this file
#    2) authentication_codes.txt
#        * authentication codes should be newline seperated with no whitespace
#          codes that are used will be commented out with a # and a space at the
#          beginning of the line
#        * you can also put your own comments in this file by putting # and a space at
#          the beginning of any line

def get_auth_code():
    auth_codes = []
    auth_code_to_return = None
    
    with open('authentication_codes.txt', 'r') as file_read:
        auth_codes = file_read.readlines()
    
    auth_code_to_return = None
    
    for i in range(len(auth_codes)):
        if not auth_codes[i].startswith('# '):
            auth_code_to_return = auth_codes[i]
            auth_codes[i] = '# {code}'.format(code=auth_codes[i])
            break
    
    with open('authentication_codes.txt', 'w') as file_write:
        file_write.writelines(auth_codes)
    
    return auth_code_to_return

# first element of returned list is email
# second element is password
def get_email_and_password():
    with open('utd_email_and_pass.txt', 'r') as file:
        return list(map(lambda x: x.strip(), file.readlines()))

def main(argv):
    with Browser('chrome', headless=False) as browser:
        [email, password] = get_email_and_password()
        
        browser.visit('https://outlook.office.com/mail/inbox/')
        
        sleep(3)
        
        email_input = browser.find_by_id('i0116').first
        email_input.fill(email)
        
        next_button = browser.find_by_id('idSIButton9').first
        next_button.click()
        
        sleep(3)
        
        password_input = browser.find_by_id('i0118').first
        password_input.fill(password)
        
        sign_in_button = browser.find_by_id('idSIButton9').first
        sign_in_button.click()
        
        sleep(3)
        
        enter_auth_code_button = browser.find_by_id('passcode').first
        enter_auth_code_button.click()
        
        auth_input = browser.find_by_css('input[class="passcode-input"]').first
        auth_input.fill(get_auth_code())
        
        sleep(60*5)
    
if __name__ == '__main__':
    main(sys.argv[1:])
    #print(get_auth_code())
    #print(get_email_and_password())