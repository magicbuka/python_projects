#8.5.1. Проверьте по коду результата, что отправка данных с помощью POST на сервер httpbin.org пройдёт корректно.
import json
import requests

def post_data(resourse, data):
    r = requests.post(resourse, data = resourse)
    if r.status_code == 200:
        print("Данные успешно отправлены")
    else:
        print("ERROR", r.status_code)
    

post_data('http://httpbin.org/post', {'UserId':'12345', 'Status':'On'})

#8.5.2. Выберите для эксперимента произвольный сайт и распарсьте из него интересующие вас значения.
from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.kinopoisk.ru/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html5lib")
    lst_names = soup.find_all('span', {'class': 'styles_title__3W58b'})
    lst_year_genre = soup.find_all('span', {'class': 'styles_subtitle__1OhKG'})

print('Сейчас в кино:')
for name, info in zip(lst_names, lst_year_genre):
    print('Название фильма:', name.text, 'Жанр:', info.text.split(',')[1])