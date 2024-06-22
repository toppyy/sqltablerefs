import sys
import re
from tests.test_runner  import run_tests


def preprocess(query):
    query = query.replace("\n", " ")
    query = query.replace("\t", " ")
    # Ensure following characters are separated from others with a space
    chars = ["(",")","=","+","-","<",">"]
    for char in chars:
        query = query.replace(char, f" {char} ")
    query = re.sub("\s+", " ", query)
    return query

def tokenise(query):
    return [token for token in query.split(" ") if len(token) > 0]

def sqltablerefs(q):

    q       = preprocess(q)
    tokens  = tokenise(q)    
    result = []
    prev = tokens.pop()

    while len(tokens) > 0:
        cur = tokens.pop()
        if cur.upper() in ["FROM","JOIN"]:
            if prev != "(":
                result.append(prev)
        prev = cur
    return set(result)
    
    
if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise Exception("Either specify a .sql file or 'test' to run tests.")

    if sys.argv[1] == 'test':
        run_tests("./tests/tests/", sqltablerefs)
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
    