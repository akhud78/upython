# Начало работы
&#127891; [Welcome To CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython?view=all) 

## Установка CircuitPython

!!! warning "Внимание"
    Сохраните свой старый код перед обновлением прошивки устройства!

- Скачайте последнюю версию [CircuitPython](https://circuitpython.org/board/espressif_esp32s3_devkitc_1_n8r2/). Нужен файл с расширением `bin`.
- Подключите плату `ESP32-S3-DevKitC` к компьютеру через micro-USB разъем с маркировкой `USB`.
- Переведите плату в загрузочный режим:
    - Удерживайте кнопку `BOOT`.
    - Нажмите и отпустите кнопку `RESET`.
    - Отпустите кнопку `BOOT`.

### Обновление через веб службу

- Откройте [ESP Web Flasher](https://adafruit.github.io/Adafruit_WebSerial_ESPTool/) с помощью браузера [Chrome](https://www.google.com/intl/ru_ru/chrome/) версии `89` или новее.
- Установите скорость `230400 Baud`. 
- Нажмите кнопку `Connect` и выберите соответствующий порт.
- После успешного определения устройства нажмите кнопку `Erase` для очистки памяти. 
- Нажмите верхнюю кнопку `Choose a file...` и выберите файл с прошивкой.
- Нажмите кнопку `Program` и после завершения обновления прошивки нажмите `Disconnect`.

### Обновление с помощью `esptool`
- Установите через менеджер пакетов [pip](https://pip.pypa.io/en/stable/getting-started/) утилиту [esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/index.html).
```bash
$ pip install esptool
```
- Обновите прошивку. После обновления нажмите `RESET`.
```bash
$ esptool.py --port /dev/ttyACM0 erase_flash
$ esptool.py --chip esp32s3 --port /dev/ttyACM0 write_flash -z 0 \
  adafruit-circuitpython-espressif_esp32s3_devkitc_1_n8r2-en_GB-8.2.2.bin
```

## Старт системы

На компьютере должен появится диск `CIRCUITPY` с каталогом `lib` и несколькими файлами. После старта `CircuitPython` ищет на своем диске  файл `code.py` и запускает его на исполнение. После обновления прошивки в нем содержится единственная строка `print("Hello World!")`. Обратите внимание, что любое изменение файлов на диске `CIRCUITPY` вызывает перезагрузку устройства.

Файл `boot_out.txt` содержит информацию об установленной версии `CircuitPython`.

```
Adafruit CircuitPython 8.2.2 on 2023-07-31; ESP32-S3-DevKitC-1-N8R2 with ESP32S3
Board ID:espressif_esp32s3_devkitc_1_n8r2
UID:C7FD1A2EB602
```

## Запуск скрипта

- Для написания кода можно использовать любой текстовый редактор.
    - Простые комментарии начинаются со знака `#`.
    - Блок кода определяется **одинаковым** количеством пробелов в начале строки (обычно четыре).
- Откройте файл `code.py` и скопируйте туда данный скрипт.
- Сохраните файл. Через несколько секунд RGB светодиод на плате выдаст серию вспышек.
- При нажатии на кнопку `RESET` произойдет перезагрузка устройства и скрипт запустится вновь.

```py
import time                                     # 1
import board
import neopixel_write
import digitalio

pin = digitalio.DigitalInOut(board.NEOPIXEL)    # 2
pin.direction = digitalio.Direction.OUTPUT
led_off = bytearray([0, 0, 0])
led_on = bytearray([0, 0, 255])     # blue

for _ in range(10):                             # 3
    neopixel_write.neopixel_write(pin, led_on)
    time.sleep(0.1)
    neopixel_write.neopixel_write(pin, led_off)
    time.sleep(0.1)
```

1. С помощью `import` происходит загрузка необходимых модулей.
2. Модуль [digitalio](https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html#module-digitalio) содержит класс для работы с цифровыми входами и выходами. Здесь определяется переменная `pin` для цифровой линии, а также задаются ее свойства.
3. В цикле `for` происходит переключение состояния RGB светодиода с некоторой задержкой, которая выполняется с помощью команды [sleep](https://docs.circuitpython.org/en/latest/shared-bindings/time/index.html#time.sleep).
