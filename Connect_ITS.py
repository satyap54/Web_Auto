#!/usr/bin/env python3
from selenium import webdriver
import os

browser=webdriver.Firefox()
browser.get('http://gstatic.com/generate_204')
#button_to_click=browser.find_element_by_css_selector('div.fer:nth-child(7) > input:nth-child(1)')
user_name=browser.find_element_by_css_selector('#un')
user_name.send_keys('ID') #put your ID here.

pswd=browser.find_element_by_css_selector('#pd')
pswd.send_keys(os.environ["ID_PASS"]) #initialize your ID_PASS var. in .bashrc to your password to login to ITS
pswd.submit()
#ele=browser.find_element_by_css_selector('#items > ytd-mini-guide-entry-renderer:nth-child(1)')
