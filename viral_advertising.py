# Viral Advertising
# HackerLand Enterprise is adopting a new viral advertising strategy.
# When they launch a new product, they advertise it to exactly 5 people on social media.
# On the first day, half of those 5 people like the advertisement and each shares it with 3 of their friends.
# how many people have liked the ad by the end of a given day.


def viral_advertising(n):
    liked = 2
    cumulative = 2

    for i in range(n-1):

        liked = liked * 3 // 2
        cumulative += liked
    return cumulative


n = int(input())
result = viral_advertising(n)
print(result)