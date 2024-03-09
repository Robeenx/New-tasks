"""
Ваша задача — написать функцию, принимающую два аргумента. n, m и возвращает отсортированный
массив всех чисел из nк mвключительно, которые имеют всего 3 делителя (1 и само число не включены).
Пример:

solution(2, 20) -> [16]

16имеет 3 делителя: 2, 4, 8 ( 1и 16не включены)
Вход:

    n- целое число (2 ≤ n ≤ 10^10)
    m- целое число (20 ≤ m ≤ 10^18)

Выход:

    result- массив целых чисел


"""


def find_x_in_range(n: int, m: int) -> list[int]:
    """
    Поиск всех чисел имеющих ровно 3 делителя (кроме самого числа и единицы) из заданного диапазона.
    """
    return [x**4 for x in range(*[int(-(-(x**(1/4))//1)) for x in (n, m + 1)]) if next((0 for i in range(2, int(x**.5)+1) if not x % i), 1 < x)]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((2, 100), [16, 81]),
        ((10000, 100000), [14641, 28561, 83521]),
        ((624, 625), [625]),
        ((625, 626), [625]),
        ((734, 735), []),
    )
    for key, val in data:
        assert find_x_in_range(*key) == val


if __name__ == '__main__':
    test()
