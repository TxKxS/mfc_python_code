from globals import tens_list

def points_calculator(hand = []):

    total = 0
    temp_hand = hand.copy()

    #Calculates total points
    for x in hand:
        if x in tens_list:
            total += 10
        elif x == 'A':
            total += 11
        else:
            total += int(x)

    while 'A' in temp_hand and total > 21:
        total -= 10
        temp_hand.remove('A')

    return total
