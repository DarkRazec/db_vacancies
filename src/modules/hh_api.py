import requests
import json
from src.modules.vacancy_api import VacancyAPI


class HeadHunterAPI(VacancyAPI):
    """Класс для работы с API сервисом 'api.hh.ru'"""
    url: str

    def __init__(self):
        self.__url = 'https://api.hh.ru/'

    def get_vacancies(self, employer_id: int, search_num: int = 0, page: int = 0) -> list[dict]:
        """
        Обращается к API сервису и возвращает список вакансий
        :param employer_id: ID компании
        :param search_num: Количество элементов выдачи (макс. 100)
        :param page: Номер страницы
        :return: Список словарей
        """
        params = {
            'employer_id': employer_id,
            'order_by': 'relevance',
            'per_page': search_num if search_num > 0 else 10,
            'page': page if page >= 0 else 0
        }
        response = requests.get(self.__url + 'vacancies', params=params)
        response.raise_for_status()
        return response.json()['items']

    def get_employers(self, num=200) -> tuple:
        for i in range(num):
            response = requests.get(self.__url + 'employers/' + str(i + 1))
            data = response.content.decode()
            response.close()
            company = json.loads(data)
            try:
                if company['open_vacancies'] == 0:
                    continue
                yield company['id'], company['name']
            except KeyError:
                continue
