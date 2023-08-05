"""
Представьте, что вам дали две палки. Вы хотите получить три
палочки одинаковой длины. Для этого вам разрешается отрезать
одну или обе палочки, а оставшиеся кусочки вы можете выбросить.

Напишите функцию maxlen, которая берет длины двух палочек
(L1 и L2, обе положительные величины), и возвращает максимальную
длину, которую вы можете сделать из трех палочек.
"""


def maxlen(L1: int, L2: int) -> int | float:
    """Поиск максимальной длины для создания 3-х палочек из 2-х."""
    return max(min(max(L1, L2) / 2, L1, L2), max(L1, L2) / 3)


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ((5, 12), 5),
        ((12, 5), 5),
        ((5, 17), 5.666666666666667),
    )
    for key, val in data:
        assert maxlen(*key) == val


if __name__ == '__main__':
    test()
