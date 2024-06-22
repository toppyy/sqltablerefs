# sqltablerefs

Python script to find all table references in a SQL-query. You might need it if you have a _bunch of_ SQL-queries and you wish to collect a list of all referenced tables.

## Usage

Provide a file to scan or 'test' for tests. Optionally a filename to store output to.

    python3 sqltablerefs.py query.sql [output.txt]

For example:

    python3 sqltablerefs.py my_query.sql my_results.txt

## Testing

To run tests:

    python3 sqltablerefs.py test

Tests are defined under `tests/queries/` are self-contained in that they contain the expected result wrapped in a comment and the SQL-query to test.