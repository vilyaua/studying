"""
Daniel Omelchenko, [16.06.16 19:49]
Крестики нолики можешь написать

Daniel Omelchenko, [16.06.16 19:49]
для двух игроков

Daniel Omelchenko, [16.06.16 19:49]
игроки ходят вводя координаты

Daniel Omelchenko, [16.06.16 19:50]
1 1 - левый верхний угол

Daniel Omelchenko, [16.06.16 19:50]
3 3 правый нижний

Итак, к домашнему заданию на следующий раз:
На уроке мы начали писать игру крестики нолики, то что у нас получилось я скинул в чат в файлике tic_tac_toe.py
Игра расчитана на двоих Х и О. В принципе основной функционал уже написан, осталось добавить один элемент:
Определение победителя. Для этого нужно дописать функцию get_winner:

def get_winner(field):
    # TODO определить победителя или ничью
    return False

Эта функция должна вернуть (используя конструкию return)  "X" или "О" в зависимости от того, кто победитель
если еще победителя нет, то функция должна вернуть False (или пустую строку "")
"""

def check(lines):                   # аргумент - список строк
    for line in lines:              # возвращает True, если хоть одна из строк списка состоит из одинаковых элементов
        if len(set(line)) == 1:
            return True
    return False

# функция осуществляет форматированный вывод текущего игрового поля
def print_game_array(game_array):
    line_div = '   -----------'     # с номерами строк и столбцов
    header = '    1   2   3 '
    line_num = 1
    print()
    print(header)
    print(line_div)
    for i in range(3):
        rez = ' | '.join(game_array[i])
        print('{:^3}'.format(str(line_num)) + ' ' + rez + '\n' + line_div)
        line_num += 1

# функция проверяет корректность ввода, сообщает об ошибке и возвращает True при неверном вводе, False при верном
# в качестве параметров принимает заданные пользователем номера строки и столбца, а также номер игрока
def move(line, row, player):
    x = int(line) - 1
    y = int(row) - 1

    # проверка на то, что введенные координаты соответствуют игровому полю
    if x not in range(0, 3) or y not in range(0, 3):
        print('   *** enter numeric values in range 1..3 ***')
        return True
    # проверка на то, что по введенным координатам уже не сделан ход ранее
    if game_array[x][y] != ' ':
        print('   *** enter another coords (these are used already) ***')
        return True
    else:
        # опредеояем, каким элементом ходим
        if player == 1:
             char = 'X'
        else:
            char = 'O'
        game_array[x][y] = char     # Осуществляем ход по заданным координатам
        return False

game_array = list([[' ' for i in range(3)] for j in range(3)])  # заполняем игровое поле пробелами

game_round = 0  # обнуляем счетчик ходов
finish = False  # для входа в основной цикл

# цикл продолжается, пока не выполнено условие "3 в ряд"
while not finish:
    game_round += 1             # увеличиваем счетчик хода
    if game_round % 2 == 0:     # определяем порядковый номер игрока
        player = 2
    else:
        player = 1
    moving = True   # для входа в цикл
    # цикл продолжается, пока не будет произведен корректный ввод координат
    while moving:
        print_game_array(game_array)        # отображаем игровое поле
        print('Move #' + str(game_round))   # сообщаем номер хода
        coords = input('player ' + str(player) + ' moves: ').split(' ')     # ввод координат
        line = coords[0]        # строка по порядку
        row = coords[1]         # столбец по порядку
        x = int(line) - 1       # индекс элемента по вертикали
        y = int(row) - 1        # индекс элемента по горизонтали
        moving = move(line, row, player)    # производим ход вызовом функции move(line, row, player)
    # ход осуществлен, проверяем, выполнено ли условние "3 в ряд"
    if game_round > 4:          # только если у нас 5-й ход и больше

        x = int(coords[0]) - 1  # x и y - индексы, по которым будем обращаться к элементу нашего 2-мерного массива
        y = int(coords[1]) - 1

        horiz_line = ''         # инициализируем строковые переменные
        vert_line = ''
        right_diag_line = ''
        left_diag_line = ''

        for i in range(3):
            # формируем строки. содержащие все элементы по горизонтали и по вертикали от введенных координат
            horiz_line += game_array[x][i]
            vert_line += game_array[i][y]
            # а также две диагональные линии - "левая" (с наклоном влево) и "правая"
            left_diag_line += game_array[i][i]
            right_diag_line += game_array[i][2 - i]

        lines = []      # инициализируем список, который будет передаваться на проверку в функцию check(lines)
        # проверяем, не находится ли последние введенные координаты на "правой" диагонали
        if y == 2 - x:
            lines.append(right_diag_line)   # добавляем "правую" диагоняль для дальнейшей проверки
        # проверяем, не находится ли последние введенные координаты на "левой" диагонали
        if y == x:
            lines.append(left_diag_line)    # добавляем "левую" диагоняль для дальнейшей проверки
        lines.append(horiz_line)            # добавляем элементы по горизонтали от введенных коорднат
        lines.append(vert_line)             # добавляем элементы по вертикали от введенных коорднат

        # проверяем все варианты последнего хода на выполнение условия "3 в ряд"
        finish = check(lines)

print_game_array(game_array)                # выводим игровое поле и информацию о победителе
print('Player ' + str(player) + ' won at move #' + str(game_round) + ' with \"' + game_array[x][y] + '\"')
input('Game over... Press Enter to finish')









