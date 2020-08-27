"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    random_scores = int(input("How many random scores: "))
    for i in range(0, random_scores):
        import random
        score = random.randint(0, 100)
        grade = determine_status(score)
        print("{} = {}".format(score, grade))


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
