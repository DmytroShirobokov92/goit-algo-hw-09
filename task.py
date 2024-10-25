from typing import Dict

# Набір монет, які використовуються для розрахунків
coins = [50, 25, 10, 5, 2, 1]


# Жадібний алгоритм для вибору мінімальної кількості монет
def find_coins_greedy(amount: int) -> Dict[int, int]:
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


# Алгоритм динамічного програмування для вибору мінімальної кількості монет
def find_min_coins(amount: int) -> Dict[int, int]:
    # Створюємо масив для мінімальної кількості монет для кожної суми від 0 до `amount`
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для суми 0 монет не потрібно
    coin_used = [None] * (amount + 1)  # Зберігаємо монету, яка використана останньою

    # Головний цикл для обчислення мінімальної кількості монет
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    # Відтворення результату: монети, які забезпечують потрібну суму
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


# Приклади використання
greedy_result = find_coins_greedy(113)
dynamic_result = find_min_coins(113)

print(greedy_result, dynamic_result)
