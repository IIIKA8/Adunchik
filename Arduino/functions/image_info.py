from PIL import Image
import serial.tools.list_ports

def get_img_info(img_p, port_ad):
    img = Image.open(img_p)  # открытие картинки
    width, height = img.size  # получение размеров картинки в px
    color_mode = img.mode  # Получение инфы о цветовой модели
    ports = list(serial.tools.list_ports.comports())  # Получение инфы портов
    img = img.convert("RGB")

    print(f'Ширина: {width} px')
    print(f'Высота: {height} px')

    if color_mode == "RGB":
        r, g, b = img.split()

    counter1 = 0
    d_list = []
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

    data_str = ''
    for i, px in enumerate(d_list):
        data_str += f"{px[0]}, {px[1]}, {px[2]}."
    data_str = data_str.rstrip(".") + ";"

    print(data_str)

    port = serial.Serial(port_ad, 9600)
    port.write(data_str.encode())  # encode метод преобразования данных в байты
    port.close()
