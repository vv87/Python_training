# -*- coding: utf-8 -*-
import time
import pytest
import math
from selenium import webdriver


@pytest.mark.parametrize('links', ['236895/step/1', '236896/step/1', '236897/step/1', '236898/step/1', '236899/step/1', '236903/step/1', '236904/step/1', '236905/step/1'])
def test_stepic(browser, links):
    answer = math.log(int(time.time()))
    link = 'https://stepik.org/lesson/{}'.format(links)
    browser.get(link)
    time.sleep(2)
    browser.find_element_by_tag_name('textarea').send_keys(str(answer))
    browser.find_element_by_class_name('submit-submission').click()
    assert "Correct!", "Корректно!"
