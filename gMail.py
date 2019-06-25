#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#  Gmailでメッセージを送る

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys

if len(sys.argv) < 3:
    sys.exit('使い方: python3 gMail.py 宛先 メッセージ...')

to_address = sys.argv[1]
message = ' '.join(sys.argv[2:])

MY_ADDRESS = '' # Add your e-mail address
MY_PASSWORD = ''

browser = webdriver.Firefox()
browser.get('https://www.google.com/gmail/')

# IDの入力
id_input = browser.find_element_by_id('identifierId')
id_input.send_keys(MY_ADDRESS)
next = browser.find_element_by_id('identifierNext')
next.click()
# ちょっと待つ。WebDriverWait.until を使うほうがよいが省略。
time.sleep(1)

# パスワードの入力
password_input = browser.find_element_by_name('password')
password_input.send_keys(MY_PASSWORD)
next = browser.find_element_by_id('passwordNext')
next.click()
time.sleep(3)

# 「作成」ボタンを押す
divs = browser.find_elements_by_xpath("//div[@role='button']")
for d in divs:
    if d.text == '作成':
        d.click()
        break
time.sleep(2)

# To: を入力
to_textarea = browser.find_element_by_name('to')
to_textarea.send_keys(to_address + '\n')
time.sleep(1)

# 件名を入力
subject_input = browser.find_element_by_name('subjectbox')
subject_input.send_keys('自動送信')
time.sleep(1)

# メッセージ本文を入力
message_div = browser.find_element_by_xpath("//div[@aria-label='メッセージ本文']")
message_div.send_keys(message)
time.sleep(2)

# 「送信」ボタンを押す
divs = browser.find_elements_by_xpath("//div[@role='button']")
for d in divs:
    if d.text == '送信':
        d.click()
        break
