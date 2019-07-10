# -*- coding: utf-8 -*-
import math
import pytest
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

a = browser.find_element_by_id("input_value")
x = a.text
y = calc(x)

b = browser.find_element_by_id('answer')
b.send_keys(y)

browser.execute_script("window.scrollBy(0, 100);")

''' чтобы кликнуть на перекрытую кнопку без скролла, можно выполнить
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()'''

# кликаем чек бокс и радио батн
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()

# ждем 1 сек
time.sleep(1)

# кликаем по кнопке
browser.find_element_by_tag_name('button').click()
