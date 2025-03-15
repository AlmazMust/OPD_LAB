import requests
from bs4 import BeautifulSoup

url = 'http://www.omgtu.ru/general_information/faculties/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    faculty_list = soup.find('div', id = 'pagecontent')
    faculties = faculty_list.find_all('li')
    
    with open('faculties.txt', 'w', encoding='utf-8') as file:
        for faculty in faculties:
            faculty_name = faculty.find('a').text.strip()
            file.write(faculty_name + '\n')

    print('Список факультетов сохранен в файл faculties.txt')
else:
    print(f"Не удалось получить страницу, код ответа: {response.status_code}")
