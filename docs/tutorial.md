# Руководство
- [Welcome To CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython?view=all)
- [UF2 Bootloader Details](https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/uf2-bootloader-details)
- [Installing the UF2 Bootloader](https://esp32s3.com/install_uf2.html)

<!-- 
- [Обновление прошивки плат Iskra JS](http://wiki.amperka.ru/js:ide:dfu-firmware) 
- [Обновление прошивки ESP-32](https://docs.geoscan.aero/ru/master/instructions/pioneer-mini/settings/esp32-update.html)
- -->
## Установка

!!! warning "Внимание"
    Сохраните свой старый код перед обновлением прошивки устройства!

### Обновление прошивки через последовательный порт
- Установите через менеджер пакетов pip утилиту [esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/index.html).
```bash
$ pip install esptool
```
- Скачайте последнюю версию [CircuitPython](https://circuitpython.org/downloads?mcufamilies=esp32s3). Нужен файл с расширениенм **bin**.
- Подключите устройство к компьютеру через USB Type C разъем и обновите прошивку.
```bash
$ esptool.py --port /dev/ttyACM0 erase_flash
$ esptool.py --chip esp32s3 --port /dev/ttyACM0 write_flash -z 0 firmware.bin
```
На компьютере должен появится диск `CIRCUITPY` с каталогом `lib` и несколькими файлами. После старта `CircuitPython` ищет на своем диске  файл `code.py` и запускает его на исполнение. После обновления прошивки в нем содержится единственная строка `print("Hello World!")`. Обратите внимание, что любое изменение файлов на диске `CIRCUITPY` вызывает перезагрузку устройства.

### Обновление прошивки через UF2-загрузчик
- Скачайте последнюю версию [CircuitPython](https://circuitpython.org/downloads?mcufamilies=esp32s3). Нужен файл с расширениенм **uf2**.
- Для активизации UF2-загрузчика необходимо два раза нажать на кнопку `RST`.

!!! note "Индикация в процессе прошивки"
    Once successful, the RGB status LED(s) on the board will flash red and then stay green. A new drive will show up on your computer.

UF2-загрузчик содержится в `CircuitPython`. Если устроойство было прошито другой программой, то обновление следует выполнять через последовательный порт.

#### Подробнее про загрузчик
- [UF2 Bootloader Details](https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/uf2-bootloader-details)
- [USB Flashing Format (UF2)](https://microsoft.github.io/uf2/)


## Запуск скрипта

- Откройте файл `code.py` в тестовом редакторе и скопируйте туда данный скрипт.
- Сохраните файл. Через несколько секунд RGB светодиод на плате `YD-ESP32-S3` выдаст серию вспышек.

```python
import time
import board
import neopixel_write
import digitalio

pin = digitalio.DigitalInOut(board.NEOPIXEL)
pin.direction = digitalio.Direction.OUTPUT
led_off = bytearray([0, 0, 0])  
led_on = bytearray([255, 0, 0])  # grb

for _ in range(10):
    neopixel_write.neopixel_write(pin, led_on)
    time.sleep(0.1)
    neopixel_write.neopixel_write(pin, led_off)
    time.sleep(0.1)
```
- Для написания кода можно использовать любой текстовый редактор. 
- Из специализированных редакторов можно порекомендовать [Thonny](https://thonny.org/).



