# Руководство
- [Welcome To CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython?view=all)
## Установка
- Скачайте последнюю версию [CircuitPython](https://circuitpython.org/downloads?mcufamilies=esp32s3). 

!!! warning "Внимание"
    Сохраните свой старый код перед обновлением прошивки устройства!

- Подключите устройство к компьютеру и обновите прошивку.
```bash
$ esptool.py --port /dev/ttyACM0 erase_flash
$ esptool.py --chip esp32s3 --port /dev/ttyACM0 write_flash -z 0 firmware.bin
```
На компьютере должен появится диск `CIRCUITPY` с каталогом `lib` и несколькими файлами. После старта `CircuitPython` ищет на своем диске  файл `code.py` и запускает его на исполнение. После обновления прошивки в нем содержится единственная строка `print("Hello World!")`. Обратите внимание, что любое изменение файлов на диске `CIRCUITPY` вызывает перезагрузку устройства.

## Запуск первого скрипта

Теперь мы собираемся написать нашу программу на `Python`, так что открываем `code.py` в текстовом редакторе.

```py
# main.py -- put your code here!
import pyb
pyb.LED(4).on()
```
