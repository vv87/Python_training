# -*- coding: utf-8 -*-
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()

"""мы видим более подробную информацию о результатах запуска: было запущено два теста, один тест выполнился с ошибкой. 
Место ошибки и пояснение к ней отображаются в логе"""
