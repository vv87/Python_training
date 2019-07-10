import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html?ruler=robots"

browser = webdriver.Chrome()
browser.get(link)

one = browser.find_element_by_id('robotCheckbox').click()
two = browser.find_element_by_id('robotsRule').click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

three = browser.find_element_by_id('answer').send_keys(y)

four = browser.find_element_by_xpath('//div[1]/form/button').click()
time.sleep(3)
browser.quit()
