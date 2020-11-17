# You are in charge of the cake for a child's birthday.
# You have decided the cake will
# have one candle for each year of their total age.
# They will only be able to blow out the tallest of the candles.
#  Count how many candles are tallest.


def birthday_cake_candles(candles):
    tall_candle = max(candles)
    count = 0
    for i in candles:
        if i == tall_candle:
            count += 1
    return count


candles_li = [4, 4, 1, 3]
print(birthday_cake_candles(candles_li))
