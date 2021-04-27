from datetime import date
import math


# PEP 572 -- Assignment Expressions (walrus operator)
## https://www.python.org/dev/peps/pep-0572/#examples
print(walrus := True)

params = {"foo": "bar"}
if x := params.get("foo"):
    print(x)

inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)


# PEP 570 -- Python Positional-Only Parameters
## In the following example, parameters a and b are positional-only,
## while c or d can be positional or keyword, and e or f are required to be keywords:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


## valid call
f(10, 20, 30, d=40, e=50, f=60)

## unvalid call
## f(10, b=20, c=30, d=40, e=50, f=60)   # b cannot be a keyword argument
## f(10, 20, 30, 40, 50, f=60)           # e must be a keyword argument


# f-strings support = for self-documenting expressions and debugging
user = "eric_idle"
member_since = date(1975, 7, 31)
print(f"{user = } {member_since = }")

r = 3.8
print(f"Diameter {(diam := 2 * r)} gives circumference {math.pi * diam:.2f}")
