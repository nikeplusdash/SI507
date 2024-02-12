import math

def change(amount, coins):
    """
    Calculates the minimum number of coins needed to make change for a given amount.

    Parameters:
    amount (int): The amount for which change needs to be made.
    coins (list): The list of available coins.

    Returns:
    int: The minimum number of coins needed to make change for the given amount.
         Returns math.inf if it is not possible to make change for the given amount.
         Returns 0 if the amount is 0.
         Returns math.inf if the amount is less than 0.
         Returns math.inf if the list of coins is empty.
    """
    if amount == 0:
        return 0
    elif amount < 0:
        return math.inf
    elif len(coins) == 0:
        return math.inf
    else:
        return min(1+change(amount - coins[0], coins), change(amount, coins[1:]))

def giveChange(amount, coins):
    """
    Calculates the minimum number of coins needed to make change for a given amount.

    Parameters:
    amount (int): The amount for which change needs to be made.
    coins (list): The list of available coins.

    Returns:
    tuple: A tuple containing the minimum number of coins needed to make change for the given amount
           and the list of coins used to make the change.
           Returns (0, []) if the amount is 0.
           Returns (math.inf, []) if the amount is less than 0 or the list of coins is empty.
    """
    if amount == 0:
        return (0, [])
    elif amount < 0:
        return (math.inf, [])
    elif len(coins) == 0:
        return (math.inf, [])
    else:
        with_coin = giveChange(amount - coins[0], coins)
        without_coin = giveChange(amount, coins[1:])
        if with_coin[0] + 1 < without_coin[0]:
            return (with_coin[0] + 1, [coins[0]] + with_coin[1])
        else:
            return without_coin

if __name__ == "__main__":
    print("HW2 - Recursion: Get Change \nList of available functions - change, giveChange")