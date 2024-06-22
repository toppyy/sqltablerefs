/*
    expected: uber_request_logs
*/
SELECT request_mnth,
       round(avg(result), 2) AS number
FROM
  (SELECT request_mnth,
          CAST(abs(division_result_one-division_result_two) AS decimal) AS result
   FROM
     (SELECT to_char(CAST(request_date AS date), 'YYYY-MM') AS request_mnth,
             distance_to_travel/monetary_cost AS division_result_one,
             sum(distance_to_travel) OVER (PARTITION BY to_char(CAST(request_date AS date), 'YYYY-MM')) / sum(monetary_cost) OVER (PARTITION BY to_char(CAST(request_date AS date), 'YYYY-MM')) AS division_result_two
      FROM uber_request_logs) a) b
GROUP BY request_mnth