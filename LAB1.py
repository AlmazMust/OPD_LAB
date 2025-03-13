import requests
from bs4 import BeautifulSoup

url = 'http://www.omgtu.ru/general_information/faculties/'

response = requests.get(url)

if response.status_code == 200
