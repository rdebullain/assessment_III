"""
 - Connect to the hr.db (stored in supporting-files directory) with sqlite3 
 - Write a query to find the names (first_name, last_name) of the employees who have a manager who works for a department based in the United States. 
 

Expected columns:
    - first_name	
    - last_name	
    - manager_od

Notes:
    - Use tables employees, departments and locations
    - You shouldn’t use JOINs here. 
    - You can connect to DB from Jupyter Lab/Notebook, explore the table and try different queries
    - In the variable 'SQL' store only the final query ready for validation 
"""


# Query to find the names of employees who have a manager in a US-based department using CTEs
SQL = """
WITH us_locations AS (
    SELECT location_id
    FROM locations
    WHERE country_id = 'US'
),
us_departments AS (
    SELECT department_id
    FROM departments
    WHERE location_id IN (SELECT location_id FROM us_locations)
),
us_managers AS (
    SELECT employee_id AS manager_id
    FROM employees
    WHERE department_id IN (SELECT department_id FROM us_departments)
)
SELECT 
    e.first_name, 
    e.last_name, 
    e.manager_id
FROM 
    employees e
WHERE 
    e.manager_id IN (SELECT manager_id FROM us_managers);
"""
