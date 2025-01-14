"""
История:
Алекс – большой поклонник снукера, и ему нравится записывать результаты своих
любимых игроков, записывая шары, попадающие в лузы стола. Он просит вас помочь
ему с программой, которая по его записям подсчитывает очки, набранные игроком
в заданном сете.

К сожалению, в его записях полный беспорядок...
Задача:
Учитывая его короткую запись в виде строки, подсчитайте очки, которые игрок
набрал в сете.

Он кодирует цвета шаров буквами:

    R = красный (1 балл)
    Y = желтый (2 балла)
    G = зеленый (3 балла)
    Bn = коричневый (4 балла)
    Быть = синий (5 очков)
    P = розовый (6 баллов)
    Bk = черный (7 очков)
    W = белый (нет очков, потому что это нарушение)

За цветом может следовать цифра «R12», обозначающая 12 забитых красных шаров.
Если номер не указан, значит, мяч был забит один раз.
"R15P3G1Bk4Y1Bn1Be3" or "R13Bk14YRGBnBkRBePBk1"

Иногда Алекс забывает, что уже записал цвет, и записывает его несколько раз.

Для вашего удобства баллы за каждый цвет представлены в виде хеша/словаря с
именем «blz».

Если строка содержит белый шар (символ «W») — возврат 'Foul'
например: "G9G11P9Bn2Bn1Be10G7WBn10G3"
Если сумма баллов больше 147 – 'invalid data'
например: "Bn14Bn14Bn8P9"
"""


import re
from operator import mul


blz = {'R': 1, 'Y': 2, 'G': 3, 'Bn': 4, 'Be': 5, 'P': 6, 'Bk': 7}


def frame(s: str) -> int | str:
    """
    Подсчитывает кол-во очков в игре.
    """
    x = re.sub(r'([A-Z][a-z]?)(\d*)', r'\1.\2 ', s).split()
    x = sum(mul(*[int(x or 1) if i else blz.get(x, 0) for i, x in enumerate(x.split('.'))]) for x in x)
    return 'Foul' if 'W' in s else 'invalid data' if 147 < x else x


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("R15Bk16YGBnBeP", 147),
        ("R15Bk14YGBnBePBk2", 147),
        ("R15Bk14YGBnBkBePBk1", 147),
        ("R13Bk14YRGBnBkRBePBk1", 147),
        ("RBk"*15 + "YGBnBePBk", 147),
        ("Bk16YGBnBeP", 132),
        ("R13Bk14YRGBnBkRBeP", 140),
        ("R13Y2GBnBkRBeP", 43),
        ("R13Bk14YRRBeP", 126),
        ("R9RGBn4BkRBeP", 48),
        ("R15Bk16GYGBnBeWP", 'Foul'),
        ("R15Bk14YGWBnBePBk2", 'Foul'),
        ("R8Bk17YGBnBkBePBk1", 'invalid data'),
        ("R8Bk17YGBnBk5BePBk1", 'invalid data'),
    )
    for key, val in data:
        assert frame(key) == val


if __name__ == '__main__':
    test()
