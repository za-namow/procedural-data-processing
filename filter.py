import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

cities = []
with open(os.path.join(__location__, "Cities.csv")) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


def filter_items(condition, dict_list):
    """Return a new list containing only the dictionaries that satisfy

    the given condition function.
    """
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """Aggregate values associated with aggregation_key using the

    provided aggregation function.
    """
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)


#-----
# 1. Print the average temperature of all the cities
avg_temp = aggregate(
    "temperature",
    lambda temps: sum(float(t) for t in temps) / len(temps) if temps else 0,
    cities,
)
print(avg_temp)
print()

# 2. Print all cities in Germany
germany_cities = filter_items(lambda c: c["country"] == "Germany", cities)
for city in germany_cities:
    print(city["city"])
print()

# 3. Print all cities in Spain with a temperature above 12°C
spain_warm_cities = filter_items(
    lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12, cities
)
for city in spain_warm_cities:
    print(city["city"])
print()

# 4. Count the number of unique countries
unique_countries_count = aggregate(
    "country", lambda countries: len(set(countries)), cities
)
print(unique_countries_count)
print()

# 5. Print the average temperature for all the cities in Germany
germany_temps_avg = aggregate(
    "temperature",
    lambda temps: sum(float(t) for t in temps) / len(temps) if temps else 0,
    germany_cities,
)
print(germany_temps_avg)
print()

# 6. Print the max temperature for all the cities in Italy
italy_cities = filter_items(lambda c: c["country"] == "Italy", cities)
max_italy_temp = aggregate(
    "temperature", lambda temps: max(float(t) for t in temps) if temps else None, italy_cities
)
print(max_italy_temp)