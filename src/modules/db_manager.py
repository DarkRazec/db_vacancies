import psycopg2
from data.config.config import config


class DBManager:
    def __init__(self):
        self.connect = psycopg2.connect(**config())

    def fill_db(self, vacancies) -> None:
        with self.connect as conn:
            with conn.cursor() as cur:
                with open('data/sql_files/create_tables.sql') as f:
                    cur.execute(f.read())
                for vacancy in vacancies:
                    insert = ("INSERT INTO vacancies (vacancy_name, company_name, vacancy_url, salary_from, salary_to, "
                              "salary_currency) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (vacancy_url) DO NOTHING;")
                    cur.execute(insert, (vacancy.name, vacancy.company, vacancy.url, vacancy.get_from(),
                                         vacancy.get_to(), vacancy.currency))

    def get_companies_vacancies_count(self):
        with self.connect as conn:
            with conn.cursor() as cur:
                query = ("SELECT DISTINCT(company_name), COUNT(vacancy_name) as vacancies_amount FROM vacancies"
                         " GROUP BY company_name;")
                cur.execute(query)
                return cur.fetchall()

    def get_all_vacancies(self):
        with self.connect as conn:
            with conn.cursor() as cur:
                query = ("SELECT vacancy_name, company_name, CONCAT('от ', salary_from, ' до ', salary_to, ' ',"
                         "salary_currency) as salary, vacancy_url FROM vacancies;")
                cur.execute(query)
                return cur.fetchall()

    def get_avg_salary(self):
        with self.connect as conn:
            with conn.cursor() as cur:
                with open('data/sql_files/avg_salary.sql') as f:
                    cur.execute(f.read())
                return cur.fetchall()[0][0]

    def get_vacancies_with_higher_salary(self):
        with self.connect as conn:
            with conn.cursor() as cur:
                with open('data/sql_files/higher_salary.sql') as f:
                    cur.execute(f.read())
                return cur.fetchall()

    def get_vacancies_with_keyword(self, user_input):
        with self.connect as conn:
            with conn.cursor() as cur:
                query = (f"SELECT * FROM vacancies WHERE vacancy_name LIKE '%{user_input.title()}%' "
                         f"OR vacancy_name LIKE '%{user_input.lower()}%'")
                cur.execute(query)
                return cur.fetchall()
