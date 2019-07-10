from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

one = browser.find_element_by_css_selector('body > form > div > div > button').click()
alert = browser.switch_to.alert
alert.accept()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


a = browser.find_element_by_id("input_value")
x = a.text
y = calc(x)

b = browser.find_element_by_id('answer')
b.send_keys(y)

four = browser.find_element_by_xpath('/html/body/form/div/div/button').click()
time.sleep(5)
browser.quit()
