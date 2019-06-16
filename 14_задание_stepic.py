# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# ждем, когда цена дома уменьшится до 10000 RUR
WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )

message = browser.find_element_by_id("book").click()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


a = browser.find_element_by_id("input_value")
x = a.text
y = calc(x)

b = browser.find_element_by_id('answer')
b.send_keys(y)

browser.find_element_by_xpath('/html/body/form/div/div/button').click()
