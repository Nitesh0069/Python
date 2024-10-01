# create a kbc game where user answers 
# for questions anwered. these are realated to cars
# X(twitter -->@Nitesh0069)
# ____________________________________________________________________________
# Author : Nitesh Kumar Verma  version ->0.1
# discovred the use of random.shuffle() method and using it for sholving 
# to generating random sequince of question ask each time. 
# ----------------------------------------------------------------------------
# Author : Nitesh Kumar Verma  version ->0.2
# Introduction of price pool for answering the question right
# Where from now?
# --> This program was a part of my 100days of code with harry challege
# there for may not be continued for now.
# if you can make this code better have fun making this .
# ----------------------------------------------------------------------------

import random 

# Displaying a welcome message and the quiz rules to the user
print("""Welcome to the quiz! 
Here are the rules of the quiz:
----------------------------------------------------------------------
1 --> Select your answer by entering the number from 1 to 4.
2 --> For each correct answer, your prize money increases.
----------------------------------------------------------------------
""")

# Defining prize money levels for each question
levels = [1000, 2000, 4000, 8000]
current_money = 0  # Tracks the current prize money the user has won
question_number = 1  # Keeps track of the current question number

# First question and answer validation
def question1():
    print(f"Question {question_number}: What is the most expensive car among the following?")
    print("1: Porsche 911 RSR\n2: Ferrari F430\n3: Lamborghini Aventador\n4: Toyota GR 86")
    user_answer = int(input("\tSelect your answer---> "))
    
    # The correct answer is option 1 (Porsche 911 RSR)
    if user_answer == 1:
        return True
    else:
        # Displays the correct answer if the user's answer is wrong
        print("Wrong Answer! Correct Answer is 1: Porsche 911 RSR.")
        return False

# Second question and answer validation
def question2():
    print(f"Question {question_number}: What is the best first upgrade for a new car?")
    print("1: Engine\n2: Transmission\n3: Suspension\n4: Brakes")
    user_answer = int(input("\tSelect your answer---> "))
    
    # The correct answer is option 4 (Brakes)
    if user_answer == 4:
        return True
    else:
        print("Wrong Answer! Correct Answer is 4: Brakes.")
        return False

# Third question and answer validation
def question3():
    print(f"Question {question_number}: What is the primary purpose of a blow-off valve in a turbocharged engine?")
    print("1: To increase fuel efficiency\n2: Release excess pressure from the intake system\n3: To prevent fuel leaks\n4: To reduce noise")
    user_answer = int(input("\tSelect your answer---> "))
    
    # The correct answer is option 2 (Release excess pressure from the intake system)
    if user_answer == 2:
        return True
    else:
        print("Wrong Answer! Correct Answer is 2: Release excess pressure from the intake system.")
        return False

# Fourth question and answer validation
def question4():
    print(f"Question {question_number}: Which car manufacturer produces the iconic Mustang?")
    print("1: Ford\n2: Chevrolet\n3: Toyota\n4: Nissan")
    user_answer = int(input("\tSelect your answer---> "))
    
    # The correct answer is option 1 (Ford)
    if user_answer == 1:
        return True
    else:
        print("Wrong Answer! Correct Answer is 1: Ford.")
        return False

# List containing all the question functions
questions = [question1, question2, question3, question4]

# Shuffles the order of the questions to make the quiz random every time
random.shuffle(questions)

# Loop through each question and check the user's answers
for question in questions:
    result = question()  # Calls the current question function
 
 
#  current_money = 0  as we progress the money from privious question gets added to courrent
# one making it better.
# question_number = 1 
 
    
    if result:
        # Increases prize money based on the correct answer and the question number
        current_money += levels[question_number - 1]
        # current_money = current_money+ levels[question_number -1 ]
        #  -1 is invloed becaue list starts form 0 not one 
        print(f"Correct Answer! Your current prize money is: ₹{current_money}")
    else:
        # Ends the game if the answer is incorrect and displays the final prize amount
        print(f"Game over! You take home: ₹{current_money}")
        break
    
    # Moves to the next question
    question_number += 1

# If all questions are answered correctly, display the final prize
if question_number > len(questions):
    print(f"Congratulations! You have won the maximum prize of ₹{current_money}")
