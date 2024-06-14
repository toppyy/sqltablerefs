/*
    expected: somedb.andschema.employee
*/
SELECT
  first_name,
  last_name,
  salary
FROM somedb.andschema.employee e1
WHERE salary >
    (SELECT AVG(salary)
     FROM somedb.andschema.employee e2
     WHERE e1.departmet_id = e2.department_id)