WITH avg_salary AS (SELECT ((SELECT AVG((salary_from + salary_to)/2) FROM vacancies WHERE salary_from > 0 AND salary_to > 0) + (SELECT AVG(salary_from) FROM vacancies WHERE salary_from > 0 AND salary_to = 0) + (SELECT AVG(salary_from) FROM vacancies WHERE salary_from = 0 AND salary_to > 0))/3)
SELECT * FROM vacancies
WHERE (salary_from > 0 AND salary_to = 0 AND salary_from > (SELECT * FROM avg_salary))
OR (salary_to > 0 AND salary_from = 0 AND salary_to > (SELECT * FROM avg_salary))
OR (salary_to > 0 AND salary_from > 0 AND (salary_from + salary_to)/2 > (SELECT * FROM avg_salary));