"""
CP1401 - Checkpoint 2
Suggested Solutions
Please do not use/view these solutions until you have attempted
the checkpoint challenges yourself!
Use these solutions as a guide to review and improve your completed work.
"""

# Docstrings:
# This is NOT a docstring.
"""This is NOT a docstring."""


def do_something():
    """This IS a docstring."""
    print()
    """This is NOT a docstring"""


def is_valid_password(password):
    """Determine if password is considered valid or not."""
    if len(password) < 6 or " " in password:
        return False
    return True


# 1. Print a line
def question_1():
    """Test question 1."""
    print_line(40)


def print_line(length):
    """Print a line of length hyphens."""
    print("-" * length)


# 2. Is it even?
def question_2():
    """Test question 2."""
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")
    # print(is_even(6))
    # print(is_even(61))


def is_even(number):
    """Determine if an integer passed into it is even."""
    return number % 2 == 0


# 3. Get Non-empty String
def question_3():
    """Get and display a user's details."""
    name = get_nonempty_string("Name: ")
    birthplace = get_nonempty_string("Birthplace: ")
    print(f"your name is {name} and you were born in {birthplace}.")


def get_nonempty_string(prompt):
    """Get non-empty string."""
    string = input(prompt)
    while string == "":
        print("String is too short")
        string = input(prompt)
    return string


# 4. Number List
def question_4():
    """Program to make list between minimum and maximum number"""
    minimum = int(input("Minimum number: "))
    maximum = int(input("Maximum number: "))
    while maximum < minimum:
        print(f"Your maximum must be greater than {minimum}")
        maximum = int(input("Maximum number: "))
    # numbers = list(range(minimum, maximum + 1))  # Here's a way you could do this more in fewer lines than below :)
    numbers = []
    for number in range(minimum, maximum + 1):
        numbers.append(number)
    print(numbers)


# 5. Subject List
# See the other subject list file for a more advanced version of this program
def question_5():
    """Program to get and process list of subject codes."""
    subjects = []
    subject = input("Enter subject code: ")
    while subject != "":
        if len(subject) != 6:
            print("Invalid subject code")
        else:
            subjects.append(subject)
        subject = input("Enter subject code: ")
    print(f"You do these {len(subjects)} subjects: ")
    for subject in subjects:
        print(subject)
    if "CP1401" in subjects:
        print("You are cool")
    else:
        print("You could be cooler")
