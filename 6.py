# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects2.html')

a = browser.find_element_by_id('num1').text
b = browser.find_element_by_id('num2').text
x = int(a) + int(b)

s = browser.find_element_by_id('dropdown').send_keys(x)

# нажать кнопку "Отправить"
four = browser.find_element_by_xpath('//div[1]/form/button').click()
