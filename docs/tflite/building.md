# Сборка TFLite Micro

  - [TensorFlow Lite Micro for Espressif Chipsets](https://github.com/espressif/tflite-micro-esp-examples)

## Установка

- [Установить ESP-IDF](../reference/esp_idf.md)
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

## Пример

```bash
$ cd examples/hello_world/
$ idf.py set-target esp32s3
```
