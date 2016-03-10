
def changeToCoins(list_all_coins, change, knownMinList):
    # default min list of coins is all pennies
    min_list_coins = [1] * change

    # base case, if change in coins, return (1, value_of_coin)
    if change in list_all_coins:
        knownMinList[change] = [change]
        return [change]
    elif knownMinList[change] > 0:
        return knownMinList[change] 
    else:
        for coin in list_all_coins:
            # if coin value > change, skip this coin and continue
            if coin > change:
                continue

            # subtract change by coin value, and recusively call this func  
            list_coins = changeToCoins(list_all_coins, change - coin, knownMinList)

            if len(list_coins) < len(min_list_coins):
                min_list_coins = list_coins + [coin]
                knownMinList[change] = min_list_coins

    return min_list_coins

for v in [1, 2, 3, 5, 9, 13, 21, 24, 26, 63, 64, 128, 598, 1001]:
    print v, '-->', changeToCoins([25, 16, 10, 5, 1], v, [0]*(v+1))
