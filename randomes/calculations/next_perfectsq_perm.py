"""
Есть несколько идеальных квадратов с определенным свойством. Например,
число n = 256является полным квадратом, его квадратный корень равен 16.
Если мы изменим положение цифр n, мы можем получить еще один идеальный
квадрат.  625(квадратный корень = 25). С этими тремя цифрами 2, 5 и 6
мы можем получить два идеальных квадрата: [256,625]

Номер 1354896 может создать еще один 4 идеальные квадраты, имеющие вместе
с самим числом в общей сложности пять идеальных квадратов:
[1354896, 3594816, 3481956, 5391684, 6395841], будучи последним в списке,
6395841, наибольшее значение набора.

Ваша задача — найти первый идеальный квадрат выше заданного нижнего_предела,
который может сгенерировать заданное количество идеальных квадратов k и не
содержит цифры 0. Затем вернуть максимальный совершенный квадрат, который
можно получить из его цифр.

Пример со случаями, рассмотренными выше:

lower_limit = 200
k = 2 (amount of perfect squares)
result = 625

lower_limit = 3550000
k = 5 (amount of perfect squares)
result  = 6395841

Особенности случайных тестов:

100 <= lower_limit <= 1e6
2 <= k <= 5
number of tests = 45

"""

from itertools import permutations as pm


def next_perfectsq_perm(lower_limit: int, k: int) -> int:
    """
    Находит первый идеальный квадрат, выше заданного предела,
    с заданнм кол-вом идеальных квадратов при перестановке цифр.
    """
    r, n = [], int(lower_limit ** .5)
    while len(r) != k:
        n += 1
        r, c = [], str(n ** 2)
        if '0' not in c:
            for x in sorted([int(''.join(c)) for c in set(pm(c))], reverse=True):
                if (x ** .5).is_integer():
                    r.append(x)
    return r and r[0]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((100, 2), 441),
        ((100, 3), 961),
        ((100, 4), 81796),
        ((500, 2), 625),
        ((1000, 3), 9216),
        ((100000, 4), 298116),
        ((144, 2), 625),
        ((145, 2), 625),
        ((440, 2), 441),
        ((441, 2), 625),
        ((257, 2), 441),
    )
    for key, val in data:
        assert next_perfectsq_perm(*key) == val


if __name__ == '__main__':
    test()
