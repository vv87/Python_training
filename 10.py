# -*- coding: utf-8 -*-
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

one = browser.find_element_by_xpath('/html/body/form/div/div/button').click()

# Переключиться на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

a = browser.find_element_by_css_selector("#input_value")
x = a.text
y = calc(x)

b = browser.find_element_by_id('answer')
b.send_keys(y)

four = browser.find_element_by_css_selector('body > form > div > div > button').click()
time.sleep(3)
browser.quit()
