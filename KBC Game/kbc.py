# create a kbc game where user answers questions these are realated to cars


import random 
print(""""Welcome to the quiz, \nfollowing are the rules of the quiz\n
      ----------------------------------------------------------------------
      1 -->select by entring the number from 1 to 4
      2 -->for eacht correct answer you price multiplies
      ----------------------------------------------------------------------
      """)
def question1():
    print("What is the most expensive car among the following?")
    print("1: Porsche 911 RSR\n2: Ferrari F430\n3: Lamborghini Aventador\n4: Toyota GR 86 ")
    user_answer     = int(input("\tSelect your answer---> "))
    
    # logic
    if user_answer == 1:
        return("\nCorrect Answer!")
    else:
        return("\nWrong Answer! Correct Answer is 1")
    #  end of logic
    
    
def  question2():
    print("What is the best first upgrade for a new car?")
    print("1: Engine\n2: Transmission\n3: Suspension\n4: Breaks")
    user_answer     = int(input("\tSelect your answer---> "))
    
    # logic
    if user_answer == 4:
        
        return("\nCorrect Answer!")
    else:
        return("\nWrong Answer! Correct Answer is 4")
    # end of logic
    
def question3():
    print("What is the primary purpose of a blow-off valve in a turbocharged engine?")
    print("1: To increace fule efficiency\n2: Release excess pressure from the intake system\n3: To prevent fuel leaks\n4: To reduce noise")
    user_answer     = int(input("\tSelect your answer---> "))

    # logic
    if user_answer == 2:
        return("Correct Answer!")
    else:
        return("\nWrong Answer! Correct Answer is 2")
    #  end of logic
    
def  question4():
    print("Which car manufacturer produces the iconic Mustang?")
    print("1: Ford\n2: Chevrolet\n3: Toyota\n4: Nissan")
    user_input = int(input("\tSelect your answer---> "))
    
    # logic
    if user_input == 1:
        return("Correct Answer!")
    else:
        return("\nWrong Answer! Correct Answer is 1")
    #  end of logic
    
# this is in tuple as tuple is immutable data type this does not work selects only 1 among the following funtions all the research was done for random methods using chatgpt,perplexcity
#  becasue why the hell not hence in later part i made it using a list type 
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# questions = (question1, question2, question3, question4)
# print(type(questions))
# # give tuple as in result
# random_question = random.choice(questions) 
# print(random_question())


# this is the better approach
questions = [question1, question2, question3, question4] 
random.shuffle(questions)
# random.shuffle() shuffles a items in the same list when you print it give diffrent sequences

for question in questions:
    print(question())
    
# for more info refer kbc_random_select_test.py in projects folder

    