-- Write your query below
select employee_id,
CASE
    WHEN name not like 'M%' and employee_id%2 != 0 THEN salary 
    ELSE 0
END AS bonus
from employees 
order by employee_id