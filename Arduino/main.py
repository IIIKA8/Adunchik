from Arduino.funnctions.file_chooser import choose_image
from Arduino.funnctions.image_info import get_img_info

if __name__ == "__main__":
    image_path = choose_image()

    if image_path:
        print(f"Выбрано изображение: {image_path}")
        port_ad = "COM3"  # ваш порт
        get_img_info(image_path, port_ad)
    else:
        print("Отменено пользователем.")
