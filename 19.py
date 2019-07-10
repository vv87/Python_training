# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver


class TestUnit(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_css_selector("div.first_block input.first").send_keys("Data")

        second = browser.find_element_by_css_selector("div.first_block input.second").send_keys("Data")

        third = browser.find_element_by_css_selector("div.first_block input.third").send_keys("Data")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем,
        # что ожидаемый текст совпадает с текстом на странице сайта
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        self.assertEqual(browser.find_element_by_tag_name("h1").text, "Поздравляем! Вы успешно зарегистировались!", 'Error Registration 1')


    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_css_selector("div.first_block input.first").send_keys("Data")

        second = browser.find_element_by_css_selector("div.first_block input.second").send_keys("Data")

        third = browser.find_element_by_css_selector("div.first_block input.third").send_keys("Data")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем,
        # что ожидаемый текст совпадает с текстом на странице сайта
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        self.assertEqual(browser.find_element_by_tag_name("h1").text, "Поздравляем! Вы успешно зарегистировались!", 'Error Registration 2')


'''  if __name__ == "__main__":
    unittest.main()'''
