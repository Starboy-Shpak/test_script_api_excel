import re

import openpyxl
import requests

URL = 'https://jsonplaceholder.typicode.com/users'


########################
# Главная функция
########################
def create_book(url):
    book = openpyxl.Workbook()
    sheet = book.active
    sheet.title = 'Пользователи'
    sheet['A1'] = 'Имя'
    sheet['B1'] = 'Почта'
    sheet['C1'] = 'Адрес'
    sheet['D1'] = 'Координаты города'
    sheet['E1'] = 'Номер телефона'

    response = requests.get(url)
    if response.status_code == 200:
        users = response.json()

        row = 2
        for user in users:
            sheet[row][0].value = user['name']
            sheet[row][1].value = user['email']
            sheet[row][2].value = parse_address(user['address'])
            sheet[row][3].value = parse_coordinates(user['address']['geo'])
            sheet[row][4].value = parse_phone(user['phone'])
            row += 1

            user_id = user['id']
            post_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/posts'
            post_response = requests.get(post_url)
            posts = post_response.json()
            sorted_posts = sorted(posts, key=lambda x: x['title'])

            if sorted_posts:
                sheet_id = book.create_sheet(f'Посты пользователя {user_id}')
                sheet_id['A1'] = 'Заголовок'
                sheet_id['B1'] = 'Содержание'

                new_row = 2
                for post in sorted_posts:
                    sheet_id[new_row][0].value = post['title']
                    sheet_id[new_row][1].value = post['body']
                    sheet_id.auto_filter.ref = 'A1:B1'
                    new_row += 1

        book.save('test_work_agromon.xlsx')
        book.close()
    else:
        return 'Не удалось подключиться к эндпоинту'


########################
# Дополнительные функции
########################
def parse_address(user_address):
    new_address = f'{user_address["zipcode"]}, '\
                  f'{user_address["city"]}, '\
                  f'{user_address["street"]}, '\
                  f'{user_address["suite"]}'
    return ''.join(new_address)


def parse_coordinates(crdnt):
    lat = calculate_crdnt(crdnt['lat'])
    lng = calculate_crdnt(crdnt['lng'])
    return f'{lat}, {lng}'


def calculate_crdnt(y):
    dd = float(y)
    d = dd
    m = (dd - d) * 60
    s = (dd - d - m/60) * 3600.00
    return f'{d}º{abs(m)}\'{abs(s)}\" '


def parse_phone(number):
    num = re.sub('[^0-9]', '', number)
    if len(num) == 11:
        return f'+{num[0]} ({num[1:4]}) {num[4:7]}-{num[7:9]}-{num[9:]}'
    else:
        return number


def get_data_sorted(x):
    return x['title']


def main():
    create_book(URL)


if __name__ == '__main__':
    main()
