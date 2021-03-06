# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на своём языке.
# 
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
# 
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5
text = input('Введите текст: ')
symCount = 0
maxCount = 0
for symbol in text:
  if symbol != ' ':
    symCount += 1
    if symCount > maxCount:
      maxCount = symCount
  else:
    symCount = 0
print(f'Длина самого длинного слова: {maxCount}')