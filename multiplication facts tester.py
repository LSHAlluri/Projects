# multiplication facts tester


import random   # library to help generate random numbers

def multiplication_tester(num,low_step,high_step,num_questions):
    
    print("Okay, let's test you on the multiplication table number ",num, "!")

    score = 0   # keep track of the score

    # create a list of all the values between low_step and high_step
    all_values = list(range(low_step, high_step + 1))
    random.shuffle(all_values)  # shuffle the values in the list

    # keep track of the number of questions asked
    asked_question = 0  

    # ask questions
    while asked_question < num_questions:

        # If we've used up all values, shuffle and reuse the pool
        if not all_values:
            all_values = list(range(low_step, high_step + 1))
            random.shuffle(all_values)

        # Take one number from the pool
        rand_num = all_values.pop()  

        print(f"Question {asked_question + 1}: What is {num} x {rand_num}?")

        # make sure the input is a number
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        # calculate the correct answer
        correct_answer = num * rand_num

        # check if the answer is correct
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.\n")

        asked_question += 1

    print(f"Test complete! You scored {score} out of {num_questions}.")

    # # ask questions
    # for i in range(1, num_questions):
    #     # generate a random number between low_step and high_step
    #     rand_num = random.randint(low_step,high_step+1)

    #     #ask the question
    #     print(f"what is {num} X {rand_num}: ")

    #     # validate that the input is a number
    #     try:
    #         user_answer = int(input("Your answer: "))
    #     except ValueError:
    #         print("Please enter a valid number.\n")
    #         continue

    #     # check the answer
    #     correct_answer = num * rand_num

    #     if user_answer == correct_answer:
    #         print("Correct!\n")
    #         score += 1
    #     else:
    #         print(f"Incorrect. The correct answer is {correct_answer}.\n")
    
    # # Display the score
    # print(f"Test complete! You scored {score} ")


# have the user enter the table number they want to test themselves on
# add data validitaion to ensure an integer is entered
try:
    facts_table = int(input("\nHello Sir, Please enter the table number you want to test yourself on: "))
except ValueError:
    print("Please enter a valid number.")
    exit()


low_step = 1     # lowest multiple being tested for
high_step = 20   # highest multiple being tested for
num_questions = 10 

multiplication_tester(facts_table,low_step,high_step,num_questions)


