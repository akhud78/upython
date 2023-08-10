# Сборка TFLite Micro

  - [TensorFlow Lite Micro for Espressif Chipsets](https://github.com/espressif/tflite-micro-esp-examples)

## Установка

- [Установить ESP-IDF](../reference/esp_idf.md)
- [Пример `foo_bar`][foo_bar]
- Клонировать проект

```bash
$ cd proj
$ git clone https://github.com/espressif/tflite-micro-esp-examples
$ cd tflite-micro-esp-examples/
$ git submodule update --init --recursive
```
- Установить переменные окружения и проверить версию

```bash
$ . $HOME/esp/esp-idf-v5.0.2/export.sh
$ idf.py --version
ESP-IDF v5.0.2-dirty
```

## Пример `Hello World`

```bash
$ cd examples/hello_world/
$ idf.py set-target esp32s3
```
- Сборка
```bash
$ idf.py build
```
- Загрузить программу

```bash
$ idf.py --port /dev/ttyUSB0 flash monitor
```

## Пример `Person detection`
```bash
$ cd examples/person_detection/
$ idf.py set-target esp32s3
```
- Конфигурация (проверить тип SPIRAM)
```bash
$ idf.py menuconfig
```
- Сборка
```bash
$ idf.py build
```

- Загрузить программу

```bash
$ idf.py --port /dev/ttyUSB0 flash monitor
```
- Вывод
```bash
>> detect_image 0
Total time = 54
FC time = 0
DC time = 24
conv time = 29
Pooling time = 0
add time = 0
mul time = 0
person score:95%, no person score 5%
I (6910) [esp_cli]: Time required for the inference is 56 ms

>> detect_image 1
Total time = 54
FC time = 0
DC time = 24
conv time = 29
Pooling time = 0
add time = 0
mul time = 0
person score:35%, no person score 65%
I (6910) [esp_cli]: Time required for the inference is 56 ms

...

>> detect_image 9
Total time = 54
FC time = 0
DC time = 24
conv time = 29
Pooling time = 0
add time = 0
mul time = 0
person score:82%, no person score 18%
I (6710) [esp_cli]: Time required for the inference is 56 ms

```