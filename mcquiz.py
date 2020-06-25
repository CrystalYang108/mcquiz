score = 0

# QUESTION 1
answer1 = input("Question 1: What is the color of pineapples? \nA. Blue \nB. Purple \nC. Yellow \nD. Green \nAnswer: ")
if answer1 == "C" or answer1 == "c":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    #while answer1 != "C" or answer1 != "c":
        print("Incorrect! Try again!")
        print("Score:", score)
        answer1 = input("Question 1: What are the color of pineapples? \nA. Blue \nB. Purple \nC. Yellow \nD. Green \nAnswer: ")
        if answer1 == "C" or answer1 == "c":
            score += 1
            print("Correct!")
            print("Score: ", score)
            print("\n")
# QUESTION 2
answer2 = input("Question 2: What continent is the United States in? \nA. North America \nB. South America \nC. Austrailia \nD. Europe \nAnswer: ")
if answer2 == "A" or answer1 == "a":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    #while answer1 != "C" or answer1 != "c":
        print("Incorrect! Try again!")
        print("Score:", score)
        answer2 = input("Question 2: What continent is the United States in? \nA. North America \nB. South America \nC. Austrailia \nD. Europe \nAnswer: ")
        if answer2 == "A" or answer1 == "a":
            score += 1
            print("Correct!")
            print("Score: ", score)
            print("\n")
