/*
    expected: sometable,toanothertable
*/
WITH mycte AS (
    SELECT col1
    FROM sometable
)
SELECT mycte.col1,b.col2
from mycte
    INNER JOIN toanothertable AS b ON mycte.key = b.key
