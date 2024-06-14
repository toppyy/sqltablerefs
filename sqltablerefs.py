import re

def preprocess(query: str) -> str:
    query = query.replace("\n", " ")
    query = query.replace("\t", " ")
    # Ensure following characters are separated from others with a space
    chars = ["(",")","=","+","-","<",">"]
    for char in chars:
        query = query.replace(char, f" {char} ")
    query = re.sub("\s+", " ", query)
    return query.upper()

def tokenise(query: str) -> list[str]:
    return [token for token in query.split(" ") if len(token) > 0]

def sqltablerefs(q: str) -> set[str]:

    q       = preprocess(q)
    tokens  = tokenise(q)    
    result = []
    prev = tokens.pop()

    while len(tokens) > 0:
        cur = tokens.pop()
        if cur in ["FROM","JOIN"]:
            if prev != "(":
                result.append(prev)
        prev = cur
    return set(result)
    
    