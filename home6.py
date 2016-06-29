import turtle
import time

# задаем параметры окна вывода Turtle
field_width = 800
field_height = 500
turtle.setup(field_width, field_height, None, None)     # задаем ширину, высоту и положение на экране (по центру)

# задаем константы для дальнейшего поворота turtle (юг, запад, север)
DIRECT_DOWN = 270
DIRECT_LEFT = 180
DIRECT_UP = 90

# задаем таймаут между рисунками
TIMEOUT = 2

# вводные для лестницы
x_start = -100      # стартовые координаты для лестницы
y_start = 150
stairs = 10         # количество ступенек
step = 20           # высота и ширина одной ступеньки

# вводные для лабиринта (спирали)
labyr_x = 150       # стартовые координаты для лабиринта
labyr_y = 50
spire_number = 5    # количество оборотов
resizing = 20       # ширина "коридора"

# вводные для "синусоиды"
sinus_x = -50       # стартовые координаты для "синусоиды"
sinus_y = -100
sinus_number = 10   # количество циклов (пар нижней и верхней полукругов)
radius = 10         # радиус полусфер

# функция перемещает turtle на заданную позицию с завершающим разворотом на юг
def move_to_start(x_start, y_start):    # в качестве параметром принимает координаты
    x = x_start
    y = y_start
    turtle.penup()                  # отключаем рисование
    turtle.setpos(x, y)             # перемещаем turtle
    turtle.setheading(DIRECT_DOWN)  # разворачиваем на юг
    turtle.pendown()                # включаем рисование

# функция рисует лестницу двумя вариантами (второй прямо под первым)
# аргументы: стартовые координаты, к-во ступеней, высота/ширина ступени
def draw_stairs(x_start, y_start, stairs, step):
    number_of_stairs = stairs
    size = step
    move_to_start(x_start, y_start)     # перемещаемся в начало
    turtle.color('blue')                # выбираем цвет
    # последовательные перемещения с изменением направления (влево/запад и вниз/юг)
    for i in range(number_of_stairs):
        turtle.forward(size)
        turtle.setheading(DIRECT_LEFT)
        turtle.forward(size)
        turtle.setheading(DIRECT_DOWN)
    time.sleep(TIMEOUT)                 # таймаут
    y_start -= 3 * size                 # смещаемся чуть вниз
    move_to_start(x_start, y_start)
    turtle.color('red')                 # меняем цвет
    next_x = x_start
    next_y = y_start
    # линия рисуется посредством последовательного перемещения turtle по угловым точкам (по ходу, гораздо быстрее так)
    for i in range(number_of_stairs):
        next_y -= step
        turtle.setpos(next_x, next_y)
        next_x -= step
        turtle.setpos(next_x, next_y)

# функция для рисования спирали (лабиринта)
def draw_labyrinth(labyr_x, labyr_y, spire_number, resizing):
    adding = 0              # длина рисуемого отрезка
    spires = spire_number
    x = labyr_x
    y = labyr_y
    move_to_start(x, y)     # перемещаемся в стартовую позицию
    turtle.color('green')   # меняем цвет
    # полная спираль (4 последовательных отрезка) составляется из двух пар отрезков одинаковой длины
    for i in range(spires * 2):
        adding += resizing
        for i in range(2):          # цикл для рисования пары (вертикальной и горизонтальной) линий
            turtle.forward(adding)
            turtle.right(90)

# функция для рисования "синусоиды", реализована в виде последовательного совмещения полукругов
def draw_sinus(sinus_x, sinus_y, sinus_number, radius):
    x = sinus_x
    y = sinus_y
    turtle.color('black')               # выбираем цвет
    # цикл по количеству периодов (пар верхней и нижней полукругов)
    for i in range(sinus_number):
        move_to_start(x, y)             # перемещаемся в точку, откуда будем рисовать нижнюю полусферу
        turtle.circle(radius, 180)      # рисуем нижнюю полусферу (после перемещения turtle ориентирована на юг)
        x += radius * 4                 # перемещаемся в точку, откуда будем рисовать верхнюю полусферу
        move_to_start(x, y)
        turtle.setheading(DIRECT_UP)    # меняем ориентацию на "север"
        turtle.circle(radius, 180)      # рисуем верхнюю полусферу
    move_to_start(x, y)                 # перемещаемся в конец "синусоиды"

draw_stairs(x_start, y_start, stairs, step)                 # запуск функции для рисования 2-х лестниц
time.sleep(TIMEOUT)                                         # таймаут
draw_labyrinth(labyr_x, labyr_y, spire_number, resizing)    # запуск функции для рисования лабиринта / спирали
time.sleep(TIMEOUT)                                         # таймаут
draw_sinus(sinus_x, sinus_y, sinus_number, radius)          # запуск функции для рисования "синусоиды"

turtle.mainloop()
