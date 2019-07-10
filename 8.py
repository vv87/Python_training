# -*- coding: utf-8 -*-
import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

one = browser.find_element_by_name('firstname').send_keys('Val')
two = browser.find_element_by_name('lastname').send_keys('lastname')
three = browser.find_element_by_name('email').send_keys('valerilyin@gmail.com')

cur_dir = os.path.abspath(os.path.dirname("F:/environments/"))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(cur_dir, '8_задание_stepic.txt')  # добавляем к этому пути имя файла
four = browser.find_element_by_name('file').send_keys(file_path)

four = browser.find_element_by_xpath('//div[1]/form/button').click()
time.sleep(3)
browser.quit()
