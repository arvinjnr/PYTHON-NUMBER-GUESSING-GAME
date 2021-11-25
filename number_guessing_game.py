#------------------THIS IS A NUMBER GUESSING GAME--------------------#
#------------------CREATED BY ARTHUR IGWE II----------------------#
#------------------VERSION 1.0------------------------------------#

from random import randint as randomnumber

print("\n###------THIS IS A NUMBER GUESSING GAME------###")
print("\n##------A NUMBER HAS BEEN GENERATED BETWEEN 1 AND 9------###")

def hint(number):
    if number % 2 == 0:
        return("\nHINT: THE NUMBER IS AN EVEN NUMBER")
    else:
        return("\nHINT: THE NUMBER IS AN ODD NUMBER")

# This tracks the score of the user
def compare_value(human_value,bot_value,user_score):
    if human_value == bot_value:
        user_score = user_score + 1
        return user_score
    elif human_value != bot_value and human_value != 0:
        user_score = user_score - 2
        return user_score
    else:
        return user_score

# This checks if user has won, lost or quit game and returns a message for each
def check_win(human_value,bot_value,result):
    if human_value == bot_value:
        result = "YOU ARE CORRECT!"
        return result
    elif human_value != bot_value and human_value != 0:
        result = "YOU ARE WRONG!"
        return result
    else:
        return("\nTHANK YOU FOR PLAYING :)")

bot_number_generator = randomnumber(1,9)
print(hint(bot_number_generator))
score = 0
check_result = ''
count = 0

while True:
    try:
        user_guess = int(input('\nMake your guess here ("0" to quit game): '))
        score = compare_value(user_guess,bot_number_generator,score)
        check_result = check_win(user_guess,bot_number_generator,check_result)
        print(check_result)
        count = count + 1

        #Checks if user is correct, and generates new number
        if check_result == "YOU ARE CORRECT!":
            print("\n###------You got it right, another number has been generated!------###")
            bot_number_generator = randomnumber(1,9)
            print(hint(bot_number_generator))

        #Makes sure that user can only play 3 times for each number generated when user fails consecutively
        elif count > 2 and check_result != "YOU ARE CORRECT!" and user_guess != 0:
            print("\n###------You have tried three times and failed, another number has been generated!------###")
            bot_number_generator = randomnumber(1,9)
            print(hint(bot_number_generator))
            count = 0

        if user_guess == 0:
            print("YOUR SCORE IS",score)
            break
    except:
        print("\nWRONG INPUT TRY AGAIN!")
