"""
Содержит ли массив все элементы другого массива?

Иногда вам нужно узнать, присутствуют ли все элементы одного массива в другом. Иногда ваш массив не
является набором и содержит повторяющиеся элементы, которые вы все равно хотите учитывать.

Примеры:

[1,2,3] contains [2,3]
[1,2,2,3,3,3] contains [2,3,3]
[1,2,2,3,3,3] does not contain [2,2,2,3,3] - too many 2's

И иногда нужно быть строгим.

[1.0,2.0,3.0] does not contain [1,2,3] - Floats are not Fixnums

(Но массивы также могут быть смешанными и содержать более одного типа объектов.)

Создайте метод под названием contains_all который принимает 2 аргумента, haystack массив, который
вам нужно проверить, и needle массив элементов, который вы ищете, и возвращает логическое значение
true или false.

Еще одна вещь: вы должны убедиться, что ваши массивы остались нетронутыми после сравнения. 
"""

from functools import reduce
from collections import Counter


def contains_all(m: list, n: list) -> bool:
    """
    Точное соответствие элеметнов второго масиива в первом, учитывая тип.
    """
    return reduce(lambda a, b: a & b == b, [Counter([(i, type(i)) for i in x]) for x in (m, n)])


data = (
    (([1, 2, 3], [2, 3]), True),
    (([1, 2, 3], [1, 2, 2]), False),
    (([1.0, 2.0, 3.0], [1, 2, 3]), False),
    ((['1', 2, 3.0], [1, 2, 3]), False),
)
for key, val in data:
    assert contains_all(*key) == val
