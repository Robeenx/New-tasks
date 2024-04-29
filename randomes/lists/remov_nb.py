"""

    Мой друг берет последовательность всех чисел от 1 до n (где n > 0).
    В этой последовательности он выбирает два числа: a и b.
    Он говорит, что произведение a и b должно быть равно сумме всех чисел в
    последовательности, исключая a и b.
    Учитывая число n, не могли бы вы назвать числа, которые он исключил из
    последовательности?

Функция принимает параметр: n (n всегда строго больше 0) и возвращает массив
или строку (в зависимости от языка) вида:

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]

со всем (a, b)какие возможные удаленные числа в последовательности 1 to n.

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ... будут отсортированы в
порядке возрастания буквы «а».

Бывает, что возможных вариантов несколько (а, б). Функция возвращает пустой
массив (или пустую строку), если не найдено никаких возможных чисел, что
доказывает, что мой друг не сказал правду! (Go: в этом случае return nil).
Примеры:

removNb(26) should return [(15, 21), (21, 15)]
or
removNb(26) should return { {15, 21}, {21, 15} }
or
removeNb(26) should return [[15, 21], [21, 15]]
or
removNb(26) should return [ {15, 21}, {21, 15} ]
or
removNb(26) should return "15 21, 21 15"
"""


from operator import mul, lt


def remov_nb(n: int) -> list:
    """
    Поиск в диапазоне от 1 до N возможных пар чисел,
    произведение которых равно сумме диапазона, исключая
    найденные числа.
    """
    i, s, r = [0, n], sum(range(n + 1)), []
    while lt(*i):
        a, b = s - sum(i), mul(*i)
        if a == b:
            r.extend([(*i,), (*i[::-1],)])
        i[a < b] += 1 * [1, -1][a < b]
    return sorted(r)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (100, []),
        (26, [(15, 21), (21, 15)]),
        (101, [(55, 91), (91, 55)]),
    )
    for key, val in data:
        assert remov_nb(key) == val


if __name__ == '__main__':
    test()
