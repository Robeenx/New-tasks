"""
Формат представления упорядоченного списка целых чисел заключается
в использовании списка, разделенного запятыми.

    отдельные целые числа
    или диапазон целых чисел, обозначенный начальным целым числом,
    отделенным от конечного целого числа в диапазоне тире «-».
    Диапазон включает все целые числа в интервале, включая обе
    конечные точки. Он не считается диапазоном, если он не
    охватывает как минимум 3 числа. Например "12,13,15-17"

Завершите решение так, чтобы оно принимало список целых чисел в
порядке возрастания и возвращало правильно отформатированную
строку в формате диапазона. 
"""


def format_range(arr: list) -> str:
    """
    Представление списка чисел в виде диапазона.
    """
    p, r, x = float('-inf'), [], 0
    for i, n in enumerate(arr + ['']):
        if i and p + 1 != n:
            if 2 < i - x:
                r.append('-'.join(map(str, arr[x:i:i-x-1])))
            else:
                r.extend(map(str, arr[x:i]))
            x = i
        p = n
    return ','.join(r)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14,
          15, 17, 18, 19, 20], '-6,-3-1,3-5,7-11,14,15,17-20'),
        ([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], '-3--1,2,10,15,16,18-20'),
        ([1, 2, 3, 4, 5], '1-5'),
    )
    for key, val in data:
        assert format_range(key) == val


if __name__ == '__main__':
    test()
