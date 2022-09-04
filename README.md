# Labour Exchange

Биржа труда на FastAPI/PostgreSQL

# Руководство по работе с проектом для разработчиков

## Требования

- python=3.8.10

## Настройка и установка проекта

1. Склонировать репозиторий с помощью команды:
   ```
   git clone https://github.com/alinocco/labour-exchange.git
   ```
2. Перейти в папку с проектом:
   ```
   cd labour-exchange
   ```
3. Установить **poetry**:
   ```
   pip3 install poetry
   ```
4. Активировать виртуальное окружение:
   ```
   poetry shell
   ```
5. Установить зависимости:
   ```
   poetry install
   ```
6. Установить Docker и docker-compose с [официального сайта](https://www.docker.com/products/docker-desktop)
7. Запустить сервисы в Docker (PostgreSQL):
   ```
   sudo docker-compose -f docker-compose.yaml up -d --build --remove-orphans
   ```
8. При необходимости отключить PostgreSQL, включить Docker, отключить TCP-подключения к порту :8000 и повторить шаг №7:
   ```
   sudo service docker start
   sudo service postgresql stop
   sudo lsof -t -i tcp:8000 | xargs kill -9
   ```
9. Запустить приложение:
   ```
   python main.py
   ```
