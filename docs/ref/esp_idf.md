# ESP-IDF

 - [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/v5.0.2/esp32s3/index.html)
 - [Установка ESP-IDF](https://docs.jethome.ru/ru/controllers/mcu/howto/espidf/install.html#esp-idf) &#128018;

`ESP-IDF` (Espressif’s IoT Development Framework) является официальной средой для разработки `IoT` приложений для микроконтроллеров семейства `ESP32`.

## <a name="#install"></a> Установка
 - [Standard Toolchain Setup for Linux and macOS](https://docs.espressif.com/projects/esp-idf/en/v5.0.2/esp32s3/get-started/linux-macos-setup.html)
- Установка зависимостей

```bash
$ sudo apt-get install git wget flex bison gperf python3 python3-venv cmake \
  ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
```
- Установка фреймворка версии `5.0.2`

```bash
$ mkdir -p ~/esp
$ cd ~/esp
$ git clone -b v5.0.2 --recursive https://github.com/espressif/esp-idf.git esp-idf-v5.0.2
$ cd esp-idf-v5.0.2/
$ ./install.sh
```
