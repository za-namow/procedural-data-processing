import csv, os
from pathlib import Path


class DataLoader:
    """Handles loading CSV data files."""

    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files."""
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)

    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries."""
        filepath = self.base_path / filename
        data = []

        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))

        return data


class DB:
    def __init__(self):
        self.tables = {}
    def insert(self, table):
        self.tables[table.table_name] = table
    def search(self, table_name):
        return self.tables.get(table_name)


class Table:
    def __init__(self, table_name, rows):
        self.table_name = table_name
        self.rows = list(rows)
        self.table = self.rows

    def filter(self, condition):
        filtered_rows = [row for row in self.rows if condition(row)]
        return Table(f"{self.table_name}_filtered", filtered_rows)

    def aggregate(self, aggregation_function, aggregation_key):
        values = []
        for row in self.rows:
            if aggregation_key in row:
                raw_val = row[aggregation_key]
                try:
                    values.append(float(raw_val))
                except (ValueError, TypeError):
                    values.append(raw_val)
        return aggregation_function(values)

    def join(self, other_table, key):
        other_key = {}
        for other_row in other_table.rows:
            if key in other_row:
                if other_row[key] not in other_key:
                    other_key[other_row[key]] = []
                    other_key[other_row[key]].append(other_row)

        joined_rows = []
        for row in self.rows:
            val = row.get(key)
            if val in other_key:
                for other_Row in other_key[val]:
                    merged = row.copy()
                    merged.update(other_Row)
                    joined_rows.append(merged)

        return Table(f"{self.table_name}_{other_table.table_name}", joined_rows)

    def __str__(self):
        return f"{self.table_name} : {str(self.rows)}"

loader = DataLoader()
cities = loader.load_csv("Cities.csv")
table1 = Table("cities", cities)
countries = loader.load_csv("Countries.csv")
table2 = Table("countries", countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search("cities")
print("List all cities in Italy:")
my_table1_filtered = my_table1.filter(lambda x: x["country"] == "Italy")
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x) / len(x), "temperature"))
print()

my_table2 = my_DB.search("countries")
print("List all non-EU countries:")
my_table2_filtered = my_table2.filter(lambda x: x["EU"] == "no")
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x["coastline"] == "yes").aggregate(lambda x: len(x), "coastline"))
print()

my_table3 = my_table1.join(my_table2, "country")
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x["EU"] == "no").filter(lambda x: float(x["temperature"]) < 5.0)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x["EU"] == "yes").filter(lambda x: x["coastline"] == "no")
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), "temperature"))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), "temperature"))
print()