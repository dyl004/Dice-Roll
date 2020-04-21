import random
def Dice_Roll():
    number = random.randint(1,6)
    answer = input('Would you like to roll the dice? (Type "Yes" to roll) ' )
    if answer.lower() == 'yes':
        print(number)
    else:
        print("Okay, I guess you are not feeling lucky")
Dice_Roll()

    

        
