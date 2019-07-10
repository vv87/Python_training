# -*- coding: utf-8 -*-

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')  # ответ 'Substring found'

index = s.find('Name')
if index != -1:
    print('Substring found at index {}'.format(index))

"""Substring found at index 3' - find использовать для проверки на полное совпадение и если требуется проверить, 
что некий текст является подстрокой другого текста"""
