"""
Возвращает век введенного года. Входные данные всегда будут представлять собой
4-значную строку, поэтому проверка не требуется.
Примеры

"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
"""


def what_century(s: str) -> str:
    """
    Возвращает век введенного года.
    """
    x = dict(enumerate(('th st nd rd' + ' th' * 10).split()))
    return str(n := int(s[:2]) + bool(int(s) % 100)) + x.get(n % 100, x[n % 10])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("2011", "21st"),
        ("2154", "22nd"),
        ("2259", "23rd"),
        ("1234", "13th"),
        ("1023", "11th"),
    )
    for key, val in data:
        assert what_century(key) == val


if __name__ == '__main__':
    test()