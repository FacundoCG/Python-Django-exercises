""" Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. 

She asked for your help. You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps. """

total_countries: int = int(input(""))
countries: set = set()

for i in range(total_countries):
    country: str = input("")
    countries.add(country)

print(len(countries))
