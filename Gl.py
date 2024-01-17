from PIL import Image
import serial.tools.list_ports
import numpy as np

d_list = []
def get_img_info(img_p):
    img = Image.open(img_p)  # открытие картинки
    width, height = img.size  # получение размеров картинки в px
    color_mode = img.mode  # Получение инфы о цветовой модели
    ports = list(serial.tools.list_ports.comports())  # Получение инфы портов

    print(f'Ширина: {width} px')
    print(f'Высота: {height} px')

    if color_mode == "RGB":
        r, g, b = img.split()

    counter1 = 0

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            d_list.append((r, g, b))
            counter1 += 1

    print(f"Кол-во точек на картинке: {counter1} \n")

    for port in ports:
        print(f"Порт: {port.device}")
        print(f"Описание: {port.description}")
        print(f"Производитель: {port.manufacturer}\n")

    np.savetxt('rgb_data.txt', d_list, fmt='%d')
    data = np.loadtxt('rgb_data.txt')
    data = data.astype(np.uint8)
    img = Image.fromarray(data.reshape((width, height, 3)), color_mode)
    img.show()

if __name__ == "__main__":
    img_p = "E:\Rozoviy_goose-main\krrr.jpg"
    Port_ad = "name_port"
    get_img_info(img_p)
