from main import *

run_cases = [
    (
        ("Welcome to the jungle", "txt"),
        ("Processing doc: 'Welcome to the jungle'. File Type: txt", {"txt": 1}),
    ),
    (
        ("We've got fun and games", "txt"),
        ("Processing doc: 'We've got fun and games'. File Type: txt", {"txt": 2}),
    ),
    (
        ("We've got *everything* you want honey", "md"),
        (
            "Processing doc: 'We've got *everything* you want honey'. File Type: md",
            {"txt": 2, "md": 1},
        ),
    ),
]

submit_cases = run_cases + [
    (
        ("We are the champions my friends", "docx"),
        (
            "Processing doc: 'We are the champions my friends'. File Type: docx",
            {"txt": 2, "md": 1, "docx": 1},
        ),
    ),
    (
        ("print('hello world')", "py"),
        (
            "Processing doc: 'print('hello world')'. File Type: py",
            {"txt": 2, "md": 1, "docx": 1, "py": 1},
        ),
    ),
]


def test(inputs, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    for inp in inputs:
        print(f" * {inp}")
    print(f"Expecting:")
    for out in expected_output:
        print(f" * {out}")
    counts = process_doc(*inputs)
    print(f"Actual:")
    for out in counts:
        print(f" * {out}")

    if counts == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

