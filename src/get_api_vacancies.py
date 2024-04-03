from src.modules.hh_api import HeadHunterAPI
from src.modules.vacancy import Vacancy


def get_api_vacancies(queries) -> list[Vacancy]:
    """Метод для взаимодействия пользователя с методом получения вакансий API класса"""
    hh_api = HeadHunterAPI()
    companies_vacancies = []
    for query in queries:
        raw_vacancies = hh_api.get_vacancies(query)
        companies_vacancies += [Vacancy(vacancy["name"], vacancy["alternate_url"],
                                        (vacancy["salary"]["from"], vacancy["salary"]["to"],
                                         vacancy["salary"]["currency"])
                                        if vacancy["salary"] else None,
                                        (vacancy["area"]["name"], vacancy["employer"]["name"],
                                         vacancy["schedule"]["name"],
                                         vacancy["experience"]["name"])) for vacancy in raw_vacancies]

    return companies_vacancies
