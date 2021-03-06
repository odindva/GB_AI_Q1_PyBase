# 6) Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(string):
    """Возвращает полученный аргумент с прописной первой буквой

    принимает только строчные латинские символы,
    остальные игнорирует
    """
    is_small_latin = True
    for ch in string:
        if ord(ch) > 122 or ord(ch) < 97:
            is_small_latin = False
    return str(string).capitalize() if is_small_latin else ''


strings = input('Введите строку из слов, разделенных пробелом: ').split()
strings = map(lambda word: int_func(word), strings)
print(' '.join(list(filter(None, strings))))  # Нашёл-таки красивый способ убрать пустые элементы:)
