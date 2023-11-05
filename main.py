from PIL import Image, ImageDraw

print('Генератор мемов запущен!')
print('Выберите шаблон для мема:')
print('1 - мем с котом за столом')
print('2 - мем неее/дааа')

which_file = int(input('Введите номер шаблона: '))
if which_file == 1:
    filename = 'мем_с_котом_за_столом.jpeg'
    x1 = 20
    y1 = 10
    x2 = 150
    y2 = 10

elif which_file == 2:
    filename = 'неее_дааа_мем.jpeg'
    x1 = 150
    y1 = 50
    x2 = 150
    y2 = 170
top_text = input('Введите верхний текст: ')
bottom_text = input('Введите нижний текст: ')
img = Image.open(filename)
text_print = ImageDraw.Draw(img)
text_print.text((x1, y1), top_text, fill='black')
text_print.text((x2, y2), bottom_text, fill='black')
img.show()