# sqltablerefs

Python script to find all table references in a SQL-query. You might need it if you have a _bunch of_ SQL-queries and you wish to collect all referenced tables.

Creates false positives for aliases :(

## Usage


Provide a file to scan or 'test' for tests. Optionally a filename to store output to.

    python3 query.sql|test [output.txt]


For example:

    python3 my_query.sql my_results.txt