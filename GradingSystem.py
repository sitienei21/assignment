from typing import Final
#immutable types

#str
#int
#bool
#float
#byte
#tuple-  allows repetitions and can be changed compared to the list which cannot be altered

#sutable types
#list
#set
#dic

#private var age:double:-kotlin-improved python
#it is not a must to notate the data type
#Strings are also arrays


number: int = 10
decimal: float = 2.5
active: bool = True

names = ("John", "Doe")  # This is a tuple, not a list
name: str = "John Doe"
marks: tuple = (1, 24, 5)

print(number)
print(names)
print(decimal)

# Greet Function--
def greet(name: str) ->None:
    return f"Welcome, {name.title()}!"

print(greet(f"Welcome, {name.title()}!"))
#Declarations are to be indented to the far left
age = 50

if age>20:
    print("adult")
elif age>50:
    print("adult")
else :
    print("underage")
#def means defining..
def add(x: int, y: int) -> int:
    return x + y

def area_circle(radius: float) -> float:
    PI: Final = 3.14
    return PI * (radius ** 2)

def has_passed(average: float) -> bool:
    return average >= 50 #returns true or False

def compute_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)
#Defining a student performance function...camelcase-allows definition in small letters and use of underscore
def students_performance() -> None:
    name: str = input("Enter student name: ")
    print(greet(name))
#Creation of an empty list that will store  the integer values .Initialization
    scores: list[int] = []

    for i in range(3):
        while True:
             try:
                score = int(input(f"Enter score for subject {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
             except ValueError:
                print("Please enter a valid number.")
#Initilaisation of variables
    average_score: float = compute_average(scores)
    is_pass: bool = has_passed(average_score)
#Formats
    print("\n---- Report Card ----")
    print(f"Name            : {name}")
    print(f"Scores          : {scores}")
    print(f"Average         : {average_score:.2f}")
    print(f"Status          : {'Pass' if is_pass else 'Fail'}")

    assignments_done: int = 5
    pts: float = 2.5
    total_score: float = average_score + pts

    print(f"Bonus Pts       : +{pts} for {assignments_done} assignments")
    print(f"Final Score     : {total_score:.2f}")


if __name__ == "main":#What does this doo???
    students_performance()