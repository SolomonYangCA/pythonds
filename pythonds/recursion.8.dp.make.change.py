def makeChange(list_coins, change, min_list_coins):
    for cents in range(change + 1):
        list_coins_cent = [1] * cents

        for coin in [c for c in list_coins if c < cents]:
            if len(min_list_coins[cents - coin]) + 1 < len(list_coins_cent):
                list_coins_cent = min_list_coins[cents - coin] + [coin]
       
        min_list_coins[cents] = list_coins_cent

    return min_list_coins[change]

for v in [1, 2, 3, 5, 9, 13, 21, 24, 26, 63, 64, 128, 598, 1001, 6009, 8348]:
    print v, '-->', makeChange([2000, 1000, 500, 200, 100, 25, 16, 10, 5, 1], v, [[]]*(v+2))
