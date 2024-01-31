import timeit


def find_coins_greedy(coins, amount):
    coins.sort(reverse=True)
    res = {coin: 0 for coin in coins}
    for coin in coins:
        res[coin] = amount // coin
        amount = amount % coin
    return res


def find_min_coins(coins, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    coin_used = [[] for _ in range(target_sum + 1)]

    for coin in coins:
        for i in range(coin, target_sum + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin_used[i - coin] + [coin]

    return dp[target_sum], {coin: coin_used[target_sum].count(coin) for coin in coins} #coin_used[target_sum]


if __name__ == "__main__":
    #small test
    coins = [1, 2, 5, 10, 25, 50]
    amount = 113
    # find_coins_greedy(coins, amount)))
    print(f"Жадібний алгоритм для суми {amount} та набору монет {coins}: {timeit.timeit(lambda: print(find_coins_greedy(coins, amount)), number=1)}")
    # find_min_coins(coins, amount)[1]
    print(f"Динамічний алгоритм для суми {amount} та набору монет {coins}: {timeit.timeit(lambda: print(find_min_coins(coins, amount)[1]), number=1)}")

    # medium test
    coins = [1, 2, 5, 10, 25, 50, 100, 200, 500, 1000]
    amount = 1848
    # find_coins_greedy(coins, amount)))
    print(
        f"Жадібний алгоритм для суми {amount} та набору монет {coins}: {timeit.timeit(lambda: print(find_coins_greedy(coins, amount)), number=1)}")
    # find_min_coins(coins, amount)[1]
    print(
        f"Динамічний алгоритм для суми {amount} та набору монет {coins}: {timeit.timeit(lambda: print(find_min_coins(coins, amount)[1]), number=1)}")

    # big test
    coins = [1, 2, 5, 10, 25, 50, 100, 200, 500, 1000]
    amount = 1234567
    # find_coins_greedy(coins, amount)))
    print(
        f"Жадібний алгоритм для суми {amount} та набору монет {coins}: {timeit.timeit(lambda: print(find_coins_greedy(coins, amount)), number=1)}")
    # find_min_coins(coins, amount)[1]
    print(
        f"Динамічний алгоритм для суми {amount} та набору монет {coins}: {timeit.timeit(lambda: print(find_min_coins(coins, amount)[1]), number=1)}")


    # medium non-standard test
    coins = [1, 5, 8, 14, 18, 33, 47, 155, 457]
    amount = 1848
    # find_coins_greedy(coins, amount)))
    print(
        f"Жадібний алгоритм для суми {amount} та набору монет {coins}: {timeit.timeit(lambda: print(find_coins_greedy(coins, amount)), number=1)}")
    # find_min_coins(coins, amount)[1]
    print(
        f"Динамічний алгоритм для суми {amount} та набору монет {coins}: {timeit.timeit(lambda: print(find_min_coins(coins, amount)[1]), number=1)}")
