import random
#get user input
def get_guess():
    return list(input("Hey ujer  plaz giv a inputz u will geti awardi"))
#generate computer code
def generate_code():
    digits = [str(num) for num in range(10)]
    #shuffle the digits and grab the first three
    random.shuffle(digits)
    return digits[:3]

#generate the clues//code is computer guess anb user_guess well its name is itself justified
def generate_clues(code,user_guess):
    if user_guess == code:
        return "CODE CRACKED u bhosad"
    clues = []
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match boi")
        elif num in code:
            clues.append(" ohihoyi Close")

    if clues == []:
        return ["NOPE/no/nathi/na/baaba re baaba uthaale re"]
    else:
        return clues


#run logic
print("Welcome code breaker!")
secret_code = generate_code()
clue_Report = []
while clue_Report != "CODE CRACKED u bhosad":
    guess = get_guess()
    clue_Report = generate_clues(guess, secret_code)
    print("here  ij d resulti of your gess")
    for clue in clue_Report:
        print(clue)






















