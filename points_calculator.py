from globals import tens_list

def points_calculator(hand = []):

    total = 0

    for x in hand:
        if x in tens_list:
            total += 10
        elif x == 'A':
            total += 11
        else:
            total += int(x)

    while 'A' in hand and total > 21:
        total -= 10
        hand.remove('A')

    return total
