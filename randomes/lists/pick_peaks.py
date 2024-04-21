"""
В этом ката вы напишете функцию, которая возвращает
позиции и значения «пиков» (или локальных максимумов)
числового массива.

Например, массив arr = [0, 1, 2, 5, 1, 0]
имеет пик в позиции 3 со стоимостью 5 (с arr[3]равно 5).

Выходные данные будут возвращены в виде объекта с двумя
свойствами: pos и Peaks. Оба этих свойства должны быть массивами.
Если в данном массиве нет пика, то результат должен быть {pos: [], peaks: []}.

Пример: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) должен вернуться
{pos: [3, 7], peaks: [6, 3]}

Все входные массивы будут действительными целочисленными массивами
(хотя они все равно могут быть пустыми), поэтому вам не нужно будет
проверять входные данные.

Первый и последний элементы массива не будут считаться пиками
(в контексте математической функции мы не знаем, что находится
после и до, и, следовательно, мы не знаем, пик это или нет).

Также остерегайтесь плато!!! [1, 2, 2, 2, 1]имеет пик, пока
[1, 2, 2, 2, 3]и [1, 2, 2, 2, 2]не. В случае пика плато возвращайте
только положение и значение начала плато. Например: pickPeaks([1, 2, 2, 2, 1])
возвращает {pos: [1], peaks: [2]}
"""


def pick_peaks(arr: list[int]) -> dict:
    """
    Поиск начальныйх пиковых значений и их позиций в переданном списке.
    """
    res, x = [], 0
    for i, (a, b) in enumerate(zip(arr, arr[1:]), 1):
        if a < b:
            x, n = [x, not x][not x], [i, b]
        if b < a and x:
            x = not res.append(n) and not x
    return dict(zip(('pos', 'peaks'), list(map(list, zip(*res))) or [[]] * 2))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([], {"pos": [], "peaks": []}),
        ([1, 1, 1, 1], {"pos": [], "peaks": []}),
        ([2, 1, 3, 1, 2, 2, 2, 2], {"pos": [2], "peaks": [3]}),
        ([2, 1, 3, 2, 2, 2, 2, 1], {"pos": [2], "peaks": [3]}),
        ([2, 1, 3, 2, 2, 2, 2, 5, 6], {"pos": [2], "peaks": [3]}),
        ([2, 1, 3, 1, 2, 2, 2, 2, 1], {"pos": [2, 4], "peaks": [3, 2]}),
        ([1, 2, 3, 6, 4, 1, 2, 3, 2, 1], {"pos": [3, 7], "peaks": [6, 3]}),
        ([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3], {"pos": [3, 7], "peaks": [6, 3]}),
        ([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1], {"pos": [3, 7, 10], "peaks": [6, 3, 2]}),
        ([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3], {"pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]}),
        ([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7], {'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]}),
    )
    for key, val in data:
        assert pick_peaks(key) == val


if __name__ == '__main__':
    test()