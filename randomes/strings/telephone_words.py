"""
Компании творчески используют буквы на клавиатуре, чтобы записать номер
телефона и сделать его более запоминающимся.
Пример: http://en.wikipedia.org/wiki/File:Telephone-keypad2.svg

Создайте сопоставление для вашего номеронабирателя, как указано в ссылке выше.
Ограничения:

    буквы все заглавные
    цифры 0, 1 отображаются на 0, 1 соответственно

Напишите функцию, которая принимает четыре цифры номера телефона и возвращает
список всех слов, которые можно записать с этим номером.
(Вы должны вернуть все перестановки, а не только английские слова.)
"""

from itertools import product


def telephone_words(s: str) -> set[str]:
    """
    Создает список всех возможных комбинаций слов, заданнойго номера телефона.
    """
    return set(map(''.join, product(*['..ABC.DEF.GHI.JKL.MNO.PQRS.TUV.WXYZ'.split('.')[int(n)] or n for n in s])))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("0002", set(["000A","000B","000C"])),
        ("1123", set(["11AD","11AE","11AF","11BD","11BE","11BF","11CD","11CE","11CF"])),
    )
    for key, val in data:
        assert telephone_words(key) == val


if __name__ == '__main__':
    test()
