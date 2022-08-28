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
7. Запустить сервисы в Docker (PostgreSQL, Redis):
   ```
   docker-compose -f basic-compose.yml up -d --build --remove-orphans
   ```
