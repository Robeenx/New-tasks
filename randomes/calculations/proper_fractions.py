"""
Если n — числитель, а d — знаменатель дроби, эта дробь определяется (приведенной) правильной дробью
тогда и только тогда, когда НОД(n,d)==1.

Например 5/16является правильной дробью, а 6/16нет, поскольку и 6, и 16 делятся на 2, поэтому дробь
можно уменьшить до 3/8.

Теперь, если вы рассматриваете данное число d, сколько правильных дробей можно построить, используя
d в качестве знаменателя?

Например, предположим, что d равно 15: с его помощью вы можете построить в общей сложности 8
различных правильных дробей от 0 до 1: 1/15, 2/15, 4/15, 7/15, 8/15, 11/15. , 15.13 и 15.14.

Вам нужно создать функцию, которая вычисляет, сколько правильных дробей можно построить с заданным
знаменателем:

proper_fractions(1)==0
proper_fractions(2)==1
proper_fractions(5)==4
proper_fractions(15)==8
proper_fractions(25)==20
"""


def proper_fractions(n: int) -> int:
    """
    Счиктает кол-во правильных дробей с заданным знаменателем.
    """
    i, x, r = 2, n, int(1 < n)
    while i <= n:
        for a in range(3, int(n ** .5 + 1), 2):
            if not n % a:
                t = a
                break
        else:
            if n % 2:
                return r * (n - (i != n))
        if not n % i:
            r, n = r * (i - (x == n)), n // i
        else:
            i, x = t, n
    return r


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1, 0),
        (2, 1),
        (5, 4),
        (15, 8),
        (25, 20),
        (566, 282),
        (643552, 239616),
    )
    for key, val in data:
        assert proper_fractions(key) == val


if __name__ == '__main__':
    test()
