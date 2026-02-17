"""
Day 15 - Basic Refactoring Example
Refactoring improves readability without changing behavior
"""

def is_eligible_to_vote(age: int) -> bool:
    return age >= 18


def main():
    age = int(input("Enter age: "))
    if is_eligible_to_vote(age):
        print("Eligible to vote")
    else:
        print("Not eligible to vote")


if __name__ == "__main__":
    main()
