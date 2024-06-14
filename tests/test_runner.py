import os

def parse_expected_value(test_data: str) -> tuple[list[str], str]:
    
    if test_data[:2] != '/*':
        raise Exception(f"Testdata is expected to start with '/*', got '{test_data[:2]}' instead")

    comment_end = test_data.find("*/")
    
    if comment_end < 0:
        raise Exception(f"Expected testdata to have expected output in a commented block.")

    expected = test_data[3:(comment_end-1)].strip()
    expected = expected.replace("expected: ","")
    expected = expected.replace(" ","")

    return(
        (set(expected.split(",")),test_data[(comment_end+2):])
    )

def parse_test_file(path: str) -> dict:
    with open(path, "r") as file:
        test_data = file.read()
    return parse_expected_value(test_data)
    

def test(path: str, sqltablerefs) -> tuple[bool,str]:

    expected,query = parse_test_file(path)
    result = set([ tb.lower() for tb in sqltablerefs(query) ])
    diff = result ^ expected
    if len(diff) > 0:
        return (False,f"\n\tExpected:\t{','.join(expected)}\n\tGot:\t\t{','.join(result)}.\t\n\tDiff:\t\t{','.join(diff)}")
    return (True,"ok!")

def run_tests(test_folder: str, sqltablerefs) -> bool:

    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith(".sql"):
                test_path = os.path.join(root, name)
                result, info = test(test_path, sqltablerefs)
                print(f"{test_path}: {result} -> {info}\n")
