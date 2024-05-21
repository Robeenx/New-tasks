"""
Введение

Добро пожаловать, искатель приключений.  Ваша цель — пройти лабиринт и достичь
финишной точки, не касаясь стен.  Это мгновенно убьет вас!


Задача

Вам будет предоставлен 2D массив лабиринта и массив направлений.
Ваша задача — следовать данным указаниям. Если вы достигнете конечной точки до
того, как все ваши ходы будут выполнены, вам следует вернуть  Finish.
Если вы ударитесь о какие-либо стены или выйдете за границу лабиринта,
вы должны вернуть Dead.   Если после использования всех ходов вы все еще
находитесь в лабиринте, вам следует вернуть  Lost.


Массив Maze будет выглядеть так

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

..со следующим ключом

0 = Безопасное место для прогулок
       1 = Стена
       2 = Начальная точка
       3 = точка финиша


  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"

Правила

1. Массив Maze всегда будет квадратным, т.е.  N x N,  но его размер и
содержимое будут меняться от теста к тесту. 

  2.  В финальных тестах стартовая  и  финишная  позиции изменятся.

  3. Массив направлений всегда будет в верхнем регистре и в формате
  N = север, E = восток, W = запад и S = ​​юг.

  4. Если вы достигнете конечной точки до того, как все ваши ходы будут
  выполнены, вам следует вернуть  Finish.

  5. Если вы ударитесь о какие-либо стены или выйдете за границу лабиринта,
  вам следует вернуть  Dead.

  6. Если после использования всех ходов вы все еще находитесь в лабиринте,
  вам следует вернуть  Lost.
"""


def maze_runner(maze: list[list[int]], directions: list[str]) -> str:
    """
    Определяет будет ли пройден лабиринт следуя указанным шагам.
    """
    way = dict(zip('NSWE', [(-1, 0), (1, 0), (0, -1), (0, 1)]))
    pos = next((i, x.index(2)) for i, x in enumerate(maze) if 2 in x)
    for step in directions:
        pos = x, y = tuple(map(sum, zip(way[step], pos)))
        if not all(n in range(len(maze)) for n in pos) or maze[x][y] == 1:
            return 'Dead'
        if maze[x][y] == 3:
            return 'Finish'
    return 'Lost'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    maze = [[1,1,1,1,1,1,1],
            [1,0,0,0,0,0,3],
            [1,0,1,0,1,0,1],
            [0,0,1,0,0,0,1],
            [1,0,1,0,1,0,1],
            [1,0,0,0,0,0,1],
            [1,2,1,0,1,0,1]]

    data = (
        ((maze,["N","N","N","W","W"]), "Dead"),
        ((maze,["N","E","E","E","E"]), "Lost"),
        ((maze,["N","N","N","N","N","E","E","E","E","E"]), "Finish"),
        ((maze,["N","N","N","N","N","E","E","E","E","E","W","W"]), "Finish"),
        ((maze,["N","N","N","N","N","E","E","S","S","S","S","S","S"]), "Dead"),
        ((maze,["N","N","N","N","N","E","E","S","S","E","E","N","N","E"]), "Finish"),
    )
    for key, val in data:
        assert maze_runner(*key) == val


if __name__ == '__main__':
    test()
