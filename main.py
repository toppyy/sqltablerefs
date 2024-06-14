import sys
from tests.test_runner import run_tests
from sqltablerefs import sqltablerefs



if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise Exception("Either specify a .sql file or 'test' to run tests.")

    if sys.argv[1] == 'test':
        run_tests("./tests/queries/", sqltablerefs)
        exit(0)

    with open(sys.argv[1], "r") as f:
        query = f.read()

    result = sqltablerefs(query)

    if len(sys.argv) == 2:
        print('\n'.join(result))
        exit(0)

    outputfile_path = sys.argv[2]
    with open(outputfile_path, "w") as outputfile:
        for tblref in result:
            outputfile.write(tblref + "\n")
    print(f"Wrote output to {outputfile_path}")
    

