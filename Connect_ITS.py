#!/usr/bin/env python3
from selenium import webdriver
import os

browser=webdriver.Firefox()
browser.get('http://gstatic.com/generate_204')
#button_to_click=browser.find_element_by_css_selector('div.fer:nth-child(7) > input:nth-child(1)')
user_name=browser.find_element_by_css_selector('#un')
user_name.send_keys('B118054')

pswd=browser.find_element_by_css_selector('#pd')
pswd.send_keys(os.environ["INFORMAL_MAIL_PASS"])
pswd.submit()
#ele=browser.find_element_by_css_selector('#items > ytd-mini-guide-entry-renderer:nth-child(1)')