# Rupal has a huge collection of country stamps.
# She decided to count the total number of distinct
# country stamps in her collection. She asked for your
# help. You pick the stamps one by one from a stack of  N country stamps.
n = int(input())
total_countries = set()
for i in range(n):
    country_stamps = str(input())
    total_countries.add(country_stamps)
print(len(total_countries))