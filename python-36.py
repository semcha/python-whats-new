import decimal


# PEP 498: Formatted string literals
## https://realpython.com/python-f-strings/
name = "Fred"
print(f"He said his name is {name}.")

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")  # nested fields

comedian = {"name": "Eric Idle", "age": 74}
print(f"The comedian is {comedian['name']}, aged {comedian['age']}.")


# PEP 515: Underscores in Numeric Literals
my_int = 1_000_000_000_000_000
print(my_int)