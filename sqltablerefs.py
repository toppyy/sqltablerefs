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


def peek(arr):
    if len(arr) == 0:
        raise "Peeked at an empty array!"
    return arr[0]

def eat_subquery(tokens):
    # Eat tokens until the subquery/expression in parenthesis is removed
    cur = peek(tokens)
    while cur != ')':
        if cur == '(':
            tokens.pop(0)
            eat_subquery(tokens)
        tokens.pop(0)
        cur = peek(tokens)



def find_CTEs(tokens):
    # Returns the aliases for CTEs (if any)
    # aliases are lowercased for case-insensitive comparison
    if len(tokens) == 0:
        return set()

    # Check if the query has a WITH-statement
    while len(tokens) > 0:
        if peek(tokens) == 'WITH':
            break
        tokens.pop(0)

    if len(tokens) == 0:
        # It does not -> return an empty set
        return set()

    # Remove 'WITH'
    tokens.pop(0)

    # If the SQL is syntactically correct
    # there first alias is the next token
    CTE = [tokens.pop(0)]
    tokens.pop(0) # AS

    cur = tokens.pop(0)

    while  len(tokens) > 0:
        
        if cur == '(':
            eat_subquery(tokens)
        cur = tokens.pop(0)

        if cur == ')':
            cur = tokens.pop(0)
            if cur == 'SELECT':
                break

            CTE.append(tokens.pop(0))
    
    return set([alias.lower() for alias in CTE])



def sqltablerefs(q):

    q       = preprocess(q)
    tokens  = tokenise(q)    
    result  = []
    CTEs    = find_CTEs(tokens.copy())

    prev = tokens.pop()

    while len(tokens) > 0:
        cur = tokens.pop()
        if cur.upper() in ["FROM","JOIN"]:
            if prev != "(" and prev.lower() not in CTEs:
                result.append(prev)
        prev = cur
    return set(result)
    
    
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
    