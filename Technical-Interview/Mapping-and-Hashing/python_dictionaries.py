"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

def add_location(continent, country, city):
    if continent not in locations:
        locations[continent] = {}
    if country not in locations[continent]:
        locations[continent][country] = []
    locations[continent][country].append(city)

add_location('Asia', 'India', 'Bangalore')
add_location('North America', 'USA', 'Atlanta')
add_location('Africa', 'Egypt', 'Cairo')
add_location('Asia', 'China', 'Shanghai')

def sort_by_city(country_city_mapping):
    city_country_mapping = {}
    city_country_list = []
    for country in country_city_mapping:
        for city in country_city_mapping[country]:
            city_country = "{} - {}".format(city, country)
            city_country_list.append(city_country)

    return sorted(city_country_list)

print('1')
for city in sorted(locations['North America']['USA']):
    print(city)

print('2')
for city_country in sort_by_city(locations['Asia']):
    print(city_country)
