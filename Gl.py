from PIL import Image
import os

list = []
def get_img_info(img_p):
    img = Image.open(img_p) # открытие картинки
    width, height = img.size # получение размеров картинки в px
    color = img.mode # Получение инфы о цветовой модели

    print(f'Ширина: {width} px')
    print(f'Высота: {height} px')

    if color == "RGB":
        r, g, b = img.split()
        print(f"Средний уровень яркости по каналам:")
        print(f"Красный (R): {sum(r.getdata()) / (width * height):.2f}")
        print(f"Зеленый (G): {sum(g.getdata()) / (width * height):.2f}")
        print(f"Синий (B): {sum(b.getdata()) / (width * height):.2f}")

    counter1 = 0

    for x in range(height):
        for y in range(width):
            r, g, b = img.getpixel((x, y))
            list.append((r, g, b))
            counter1 += 1

    print(list)
    print(counter1)

if __name__ == "__main__":
    img_p = "E:\Rozoviy_goose-main\krr.jpg"
    get_img_info(img_p)

