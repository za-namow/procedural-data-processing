import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
file_path = os.path.join(__location__, "Cities.csv")

class Table:
    def __init__(self, rows):
        self.rows = rows

    def filter(self, condition):
        filtered_rows = [row for row in self.rows if condition(row)]
        return Table(filtered_rows)

    def aggregate(self, aggregation_key, aggregation_function):
        values = [row[aggregation_key] for row in self.rows]
        return aggregation_function(values)


class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        rows = []
        with open(self.filepath) as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(dict(row))
        return Table(rows)


if __name__ == "__main__":
    loader = DataLoader(file_path)
    cities_table = loader.load()
    avg_temp = cities_table.aggregate(
        "temperature",
        lambda temps: sum(float(t) for t in temps) / len(temps) if temps else 0
    )
    print(avg_temp)
    print()
    germany_table = cities_table.filter(lambda c: c["country"] == "Germany")
    for city in germany_table.rows:
        print(city["city"])
    print()

    spain_warm_table = cities_table.filter(
        lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12
    )
    for city in spain_warm_table.rows:
        print(city["city"])
    print()

    unique_countries_count = cities_table.aggregate(
        "country", 
        lambda countries: len(set(countries))
    )
    print(unique_countries_count)
    print()

    germany_avg_temp = germany_table.aggregate(
        "temperature",
        lambda temps: sum(float(t) for t in temps) / len(temps) if temps else 0
    )
    print(germany_avg_temp)
    print()

    italy_table = cities_table.filter(lambda c: c["country"] == "Italy")
    max_italy_temp = italy_table.aggregate(
        "temperature", 
        lambda temps: max(float(t) for t in temps) if temps else None
    )
    print(max_italy_temp)