#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from splinter import Browser
from time import sleep
import sys

sleep_in_between_page_time_seconds = 4 # increase this if you have a slow internet connection

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
        
        sleep(sleep_in_between_page_time_seconds)
        
        email_input = browser.find_by_id('i0116').first
        email_input.fill(email)
        
        next_button = browser.find_by_id('idSIButton9').first
        next_button.click()
        
        sleep(sleep_in_between_page_time_seconds)
        
        password_input = browser.find_by_id('i0118').first
        password_input.fill(password)
        
        sign_in_button = browser.find_by_id('idSIButton9').first
        sign_in_button.click()
        
        sleep(sleep_in_between_page_time_seconds)
        
        enter_auth_code_button = browser.find_by_id('passcode').first
        enter_auth_code_button.click()
        
        auth_input = browser.find_by_css('input[class="passcode-input"]').first
        auth_input.fill(get_auth_code())
        
        sleep(sleep_in_between_page_time_seconds)
        
        daily_health_check = browser.find_by_text('Daily Health Check <redcap@utdallas.edu>').first
        daily_health_check.click()
        
        sleep(sleep_in_between_page_time_seconds)
        
        survey_link_string = browser.links.find_by_text('Daily Health Check')[0]['href']
        browser.visit(survey_link_string)
        
        if len(browser.find_by_text('Close survey') == 0:
            print('You have already completed the survey today. Make sure to do it again tomorrow!')
            sys.exit()
        
        sleep(sleep_in_between_page_time_seconds)
        
        choice_input_divs = browser.find_by_css('div[class="choicevert"')
        
        choice_yes = choice_input_divs[0].find_by_css('input')
        choice_no = choice_input_divs[1].find_by_css('input')
        
        if argv[0] == 'yes' or argv[0] == 'Yes':
            choice_yes.click()
        elif argv[0] == 'no' or argv[0] == 'No':
            choice_no.click()
        else:
            print('An answer to the survey question "Will you be on campus today?" was not found. Please try again with an argument of either "yes" or "no"')
            sys.exit()
        
        submit_button = browser.find_by_text('Submit')[0]
        submit_button.click()
        
        sleep(sleep_in_between_page_time_seconds)
        
        close_survey_button = browser.find_by_text('Close survey')[0]
        close_survey_button.click()
        
        sleep(10)
    
if __name__ == '__main__':
    main(sys.argv[1:])
    #print(get_auth_code())
    #print(get_email_and_password())