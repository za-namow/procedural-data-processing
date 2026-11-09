import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


# Print first 5 cities only
for city in cities[:5]:
    print(city)
    print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("Printing all cities in Germany")
for city in cities:
    if city["country"] == "Germany":
        print(city['city'])
        print()

# Print all cities in Spain with a temperature above 12°C

print("Printing all cities in Spain and with a temperature above 12")
for city in cities:
    if city["country"] == "Spain" and city["temperature"] > "12":
        print(city['city'])
        print()

# Count the number of unique countries

print("Count the number of unique countries")
temps = []
for city in cities:
    if city["country"] not in temps:
        temps.append(city["country"])

print(len(temps))

# for city in cities:
#     print(city['city'])
#     print()

# Print the average temperature for all the cities in Germany

print("Printing avg. temperature in Germany cities")
temps = []
for city in cities:
    if city["country"] == "Germany":
        temps.append(city["temperature"])

temps2 = 0
temps = list(map(float, temps))

for value in temps:
    temps2 += value
    temps3 = temps2/len(temps)

print(temps3)

# Print the max temperature for all the cities in Italy

print("Print the max temperature for all the cities in Italy")
temps = []
for city in cities:
    if city["country"] == "Italy":
        temps.append(city['temperature'])

temps = list(map(float, temps))
max_x = temps[0]

for value in temps:
    if value > max_x:
        max_x = value

print(max_x)