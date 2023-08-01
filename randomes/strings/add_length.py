"""
Что, если нам нужно, чтобы длина слов, разделенных пробелом,
была добавлена в конце того же слова и возвращена в виде массива?

Пример (ввод --> вывод):
"apple ban" --> ["apple 5", "ban 3"]
"you will win" --> ["you 3", "will 4", "win 3"]

Ваша задача — написать функцию, которая принимает строку и возвращает
массив/список с длиной каждого слова, добавленного к каждому элементу.

Примечание. Строка будет содержать как минимум один элемент,
слова всегда будут разделены пробелом.
"""


def add_length(string: str) -> list[str]:
    """Разбивает строку на отдельные слова, добавляя кол-во символов в слове."""
    return [f'{x} {len(x)}' for x in string.split()]


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ('y', ["y 1"]),
        ('you', ["you 3"]),
        ('apple ban', ["apple 5", "ban 3"]),
        ('you will win', ["you 3", "will 4", "win 3"]),
    )

    for key, val in data:
        assert add_length(key) == val


if __name__ == '__main__':
    test()
