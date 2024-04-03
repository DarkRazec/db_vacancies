from src.modules.db_manager import DBManager
from src.get_api_vacancies import get_api_vacancies


class UserInterface:
    """Класс для взаимодействия пользователя с модулями программы"""
    def __init__(self):
        self.db_manager = DBManager()

        while True:
            user_input = input("""
    Введите режим работы с программой:
        1 - заполнить базу данных вакансиями
        2 - показать название компаний и количество их вакансий
        3 - показать все вакансии
        4 - показать среднюю зарплату по всем вакансиям
        5 - показать вакансии с зарплатой выше средней
        6 - показать вакансии с ключевым словом в названии
        7 - выйти)
        """)
            if user_input in ("7", "выйти"):
                exit(0)
            if user_input == '1':
                companies_id = (6, 13, 42, 48, 54, 59, 19, 63, 125, 115)
                vacancies = get_api_vacancies(companies_id)
                self.db_manager.fill_db(vacancies)
            elif user_input == '2':
                print('\nКол-во вакансий', '\t', 'Название компании\n')
                [print(amount, '\t'*5, name) for name, amount in self.db_manager.get_companies_vacancies_count()]
            elif user_input == '3':
                print('\nСписок вакансий:')
                [print('\t', vacancy, company, salary, url) for vacancy, company, salary, url in self.db_manager.get_all_vacancies()]
            elif user_input == '4':
                print('\nСредняя заработная плата по вакансиям:')
                print('\t', int(self.db_manager.get_avg_salary()), 'руб.')
            elif user_input == '5':
                print('\nСписок вакансий с зарплатой выше средней:')
                [print('\t', vacancy, company, 'от', sal_from, 'до', sal_to, curr, url) for _, vacancy, company, sal_from, sal_to, curr, url in self.db_manager.get_vacancies_with_higher_salary()]
            elif user_input == '6':
                user_input = input("\nВведите ключевое слово для поиска по вакансиям: ")
                print('\nСписок вакансий с ключевым словом в названии:')
                [print('\t', vacancy, company, 'от', sal_from, 'до', sal_to, curr, url) for _, vacancy, company, sal_from, sal_to, curr, url in self.db_manager.get_vacancies_with_keyword(user_input)]
