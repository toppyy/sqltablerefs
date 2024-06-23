/*
    expected: sometable,mytable,stuff
*/
INSERT INTO stuff (col)
SELECT col1
FROM mytable
WHERE key EXISTS(
    SELECT 1
    FROM sometable
    WHERE sometable.key = mytable.key
)