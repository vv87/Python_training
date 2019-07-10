import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

a = browser.find_element_by_id('treasure')
x_element = a.get_attribute('valuex')
x = x_element
y = calc(x)

three = browser.find_element_by_id('answer')
three.send_keys(y)

one = browser.find_element_by_id('robotCheckbox')
one.click()
two = browser.find_element_by_id('robotsRule')
two.click()
time.sleep(2)
four = browser.find_element_by_tag_name('button').click()
