/*
    expected: sometable,toanothertable
*/
SELECT a.col1,b.col2
FROM sometable AS a
    INNER JOIN toanothertable AS b ON a.key = b.key
