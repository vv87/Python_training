# -*- coding: utf-8 -*-


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    sub = str(substring)
    fs = str(full_string)
    assert substring in full_string, f"'expected '{sub}' to be substring '{fs}'"


print(test_substring("fulltext", "some_value"))
# должен быть такой Assert: AssertionError: 'expected 'some_value' to be substring 'fulltext'
