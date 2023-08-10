# Фреймворк ESP-IDF

 - [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/v5.0.2/esp32s3/index.html)
 - [Standard Toolchain Setup for Linux and macOS](https://docs.espressif.com/projects/esp-idf/en/v5.0.2/esp32s3/get-started/linux-macos-setup.html)
 - [Установка ESP-IDF](https://docs.jethome.ru/ru/controllers/mcu/howto/espidf/install.html#esp-idf)

`ESP-IDF` (Espressif’s IoT Development Framework) является официальной средой для разработки `IoT` приложений для микроконтроллеров семейства `ESP32`.

##  Установка `ESP-IDF`

### Установка зависимостей

```bash
$ sudo apt-get install git wget flex bison gperf python3 python3-venv cmake \
  ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
```
### Установка фреймворка
- Версия `5.0.2`

```bash
$ mkdir -p ~/esp
$ cd ~/esp
$ git clone -b v5.0.2 --recursive https://github.com/espressif/esp-idf.git esp-idf-v5.0.2
$ cd esp-idf-v5.0.2/
$ ./install.sh
```

{!docs/reference/foo_bar.md!}
