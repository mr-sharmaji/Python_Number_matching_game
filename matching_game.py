import random
#function to input 3 digited number from user Number
def get_guess():
    n=input("What Is Your Guess?\n")
    return n

#function to generate 3 digit computer code
def computer_code():
    digits = [str(num) for num in range(10)]
#shuffle all the digits
    random.shuffle(digits)
#returning the first 3 digits
    return digits[:3]

#function to generate clues
def generate_clues(code,ug):
    if ug == code:
        return "CRACKED!! \n PARTY!!"
    clues = []

    for ind,num in enumerate(ug):
        try:
            if(num == code[ind]):
                clues.append("Match!")
            elif num in code:
                clues.append("Close!")
        except:
            print("wrong Input")
    if clues == []:
        return ["No!"]
    else:
        return clues


print("\nWelcome To Number Matching Game!\n")
cc= computer_code()
clue_result = []
while clue_result != "CRACKED!! \n PARTY!!":
    guess=get_guess()
    clue_result=generate_clues(guess,cc)
    print("Here is the result of your guess: ")
    for clue in clue_result:
        print(clue)
