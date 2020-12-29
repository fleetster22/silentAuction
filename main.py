# Day 9 of 100 Days of Code - The Complete Python Pro Bootcamp for 2021
from time import sleep
from art import logo

# programming_dictionary = {
#     "Bug": "A spider in your computer",
#     "Function": "A piece of code that you can easily call repeatedly",
#     "Loop": "The action of doing something repeatedly",
# }
# programming_dictionary["Nested"] = "A unit of code that is fully contained under another unit of code"

# print(programming_dictionary["Function"])
# edit an entry
# programming_dictionary["Bug"] = "An error in a program that prevents the program from running as expected"
# print(programming_dictionary)

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

student_scores = {
    "Harry" : 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    if 90 < student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
    elif 80 < student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 70 < student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)


# print(logo)
# sleep(0.75)
# print("Welcome to the Silent Auction Program.")
# sleep(0.5)
# name = input("What is your name?\n")
# sleep(0.15)
# print(f"Welcome, {name}")
# sleep(0.5)
# bid = input("What is your bid on this item? \n$")
# other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")
