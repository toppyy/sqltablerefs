/*
    expected: sometable,toanothertable,tbl,stuff
*/
WITH myCTE AS (
    SELECT col1,key
    FROM sometable
    WHERE EXISTS(
        SELECT 1
        FROM stuff
        WHERE stuff.key = sometable.key
    )
), anotherCTE AS (
    SELECT col2,key
    FROM toanothertable
    WHERE key IN (SELECT myCTE.key FROM myCTE)
)
SELECT tbl.col1,b.col2
from anotherCTE AS b
    LEFT JOIN tbl ON b.key = tbl.key