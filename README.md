# Скрипт на языке Python

Тестовый скрипт для:
 - получения данных по эндпоинту API
 - обработки информации по техническому заданию
 - сохранению информации в файл Excel

## Техническое задание:

Есть сайт с API

У него есть два ендпойнта:
1. Получить список пользователей - https://jsonplaceholder.typicode.com/users
2. Получить список постов пользователя - https://jsonplaceholder.typicode.com/users/<user_id>/posts

Используя это API, необходимо сгенерировать xlsx-файл следующего формата:
1. Первый лист "Пользователи". Столбцы:
    - Имя
    - Почта
    - Адрес вывести в формате "zipcode, city, street, suite"
    - Координаты города перевести в формат <градусы>°<минуты>'<секунды")
    - Номер телефона в формате +X (XXX) XXX-XX-XX, если в номере 11 цифр. Если другое кол-во - вывести как есть.
2. На следующих листах вывести посты пользователей (1 лист - 1 пользователь, если постов у пользователя нет, то лист не нужен). Добавить фильтрацию постов в лексографическом порядке.
    Столбцы:
    - Заголовок
    - Содержание

Для работы с excel использовать библиотеку openpyxl

### Как запустить проект:
Клонируем репозиторий и устанавливаем зависимости в виртуальное окружение.
***
Автор: Вадим Шпак.
Связаться со мной можно в [телеграм](https://t.me/starboy_shpak/)
