from main import *

run_cases = [(2, 2), (3, 6), (5, 120)]

submit_cases = run_cases + [
    (1, 1),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (11, 39916800),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * num_posts: {input1}")
    print(f"Expecting: {expected_output}")
    result = num_possible_orders(input1)
    print(f"Actual: {result}")
    if result == expected_output:
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

