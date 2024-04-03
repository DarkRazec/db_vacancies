SELECT ((SELECT AVG((salary_from + salary_to)/2) FROM vacancies WHERE salary_from > 0 AND salary_to > 0)
+ (SELECT AVG(salary_from) FROM vacancies WHERE salary_from > 0 AND salary_to = 0)
+ (SELECT AVG(salary_from) FROM vacancies WHERE salary_from = 0 AND salary_to > 0))/3;