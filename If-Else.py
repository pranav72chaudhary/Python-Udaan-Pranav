# WAP to verify if it is raining or not

answer = input("Is it raining? Enter Yes or No: ").lower()

if answer == "yes":
    print("Bring your umbrella")
elif answer == "no":
    print("No need of umbrella")
else:
    print("Enter valid answer")


# WAP to verify if the user is eligible to vote

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
elif age < 18:
    print("Grow up")
else:
    print("Enter valid age")


# WAP to score a student

score = int(input("Enter your score: "))

if score <= 100 and score >= 90:
    print("Grade A+")
elif score < 90 and score >= 80:
    print("Grade A")
elif score < 80 and score >= 70:
    print("Grade B+")
elif score < 70 and score >= 60:
    print("Grade B")
elif score < 60 and score >= 0:
    print("You Failed")
else:
    print("Enter valid score")


# WAP to check attendance and assignments

assign = input("Is your assignment completed? ").lower()
att = int(input("Enter your attendance: "))

if assign == "yes" and att >= 70:
    print("You can give the exam")
elif assign == "no" and att >= 70:
    print("Submit your assignment first")
elif assign == "yes" and att < 70:
    print("Your attendance is not completed")
elif assign == "no" and att < 70:
    print("Complete your assignment and attendance")
else:
    print("Enter valid answers")