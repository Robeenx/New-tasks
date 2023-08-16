"""
Вам будет предоставлен массив событий, которые представлены строками.
Строки представляют собой даты в формате ЧЧ:ММ:СС.

Известно, что все события записываются в хронологическом порядке и
два события не могут произойти в одну и ту же секунду.

Возвращает минимальное количество дней, в течение которых ведется
запись журнала. 
"""


def check_logs(log: list):
    """
    Поиск кол-ва дней ведения логов.
    """
    return sum(a >= b for a, b in zip(log, log[1:])) + bool(log)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([], 0),
        (["12:12:12"], 1),
        (['00:00:00', '00:00:01', '00:00:01'], 2),
        (["12:00:00", "23:59:59", "00:00:00"], 2),
        (["12:00:00", "12:00:00", "00:00:00"], 3),
        (["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"], 1),
    )

    for key, val in data:
        assert check_logs(key) == val


if __name__ == '__main__':
    test()
