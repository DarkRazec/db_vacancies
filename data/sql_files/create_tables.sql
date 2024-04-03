CREATE TABLE IF NOT EXISTS vacancies
(
	vacancy_id smallserial PRIMARY KEY,
	vacancy_name varchar(100),
	company_name varchar(50),
	salary_from int,
	salary_to int,
	salary_currency varchar(5) NOT NULL,
	vacancy_url varchar(50),

	CONSTRAINT unq_url UNIQUE(vacancy_url)
);