# RuStore Downloader

📦 Скрипт для скачивания приложений из магазина RuStore по их package names.

## 📥 Установка

1. Клонируйте репозиторий или скопируйте файлы в вашу Linux-систему:
   git clone https://github.com/ваш-username/rustore-downloader.git
   cd rustore-downloader

2. Создание виртуальной среды:
   python3 -m venv venv
   source venv/bin/activate

3. Установите зависимости:
   pip install -r requirements.txt

4. Установите пакет в режиме разработки:
   pip install -e .

📝 Примеры использования

# Скачать приложение СберБанк Онлайн
rustore-downloader ru.sberbankmobile

# Скачать приложение в указанную директорию
rustore-downloader ru.sberbankmobile -d ~/Downloads

# Включить подробный вывод
rustore-downloader ru.sberbankmobile -v
