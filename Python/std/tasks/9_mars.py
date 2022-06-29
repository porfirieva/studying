# К роботу Валли отправили ещё одного робота Билли.
# Это его первый поход на Марс,
# поэтому он тестируется в прямоугольном помещении размером 15 на 20 метров.
# Марсоход высаживается в центре комнаты (в точке 8, 10),
# после чего управление им передаётся оператору - пользователю вашей программы.
# 
# Программа спрашивает
# в какую сторону оператор хочет направить робота:
# север (клавиша W),
# юг (клавиша S),
# запад (клавиша A)
# или восток (клавиша D).
# 
# Оператор делает выбор,
# марсоход перемещается на 1 метр в эту сторону и программа сообщает новую позицию марсохода.
# Если марсоход упёрся в стену,
# то он не должен пытаться перемещаться в сторону стены, в этом случае его позиция не меняется.
# 
# Пример:
# 
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
stepX = 8
stepY = 10
step = input(f'Марсоход находится на позиции {stepX}, {stepY}, введите команду: ')

while True:
  if step == 'W':
    if stepX != 0:
      stepX -= 1
      step = input(f'Марсоход находится на позиции {stepX}, {stepY}, введите команду: ')
    else:
      step = input(f'Марсоход находится на позиции {stepX}, {stepY}, введите команду: ')
  if step == 'S':
    if stepX != 15:
      stepX += 1
      step = input(f'Марсоход находится на позиции {stepX}, {stepY}, введите команду: ')
    else:
      step = input(f'Марсоход находится на позиции {stepX}, {stepY}, введите команду: ')
  if step == 'A':
    if stepY != 0:
      stepY -= 1
      step = input(f'Марсоход находится на позиции {stepX}, {stepY}, введите команду: ')
    else:
      step = input(f'Марсоход находится на позиции {stepX}, {stepY}, введите команду: ')
  if step == 'D':
    if stepY != 20:
      stepY += 1
      step = input(f'Марсоход находится на позиции {stepX}, {stepY}, введите команду: ')
    else:
      step = input(f'Марсоход находится на позиции {stepX}, {stepY}, введите команду: ')