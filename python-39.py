# PEP 584 -- Add Union Operators To dict
x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}
print(x | y)
print(y | x)

## dictionary in place update
libraries = {
    "collections": "Container datatypes",
    "math": "Mathematical functions",
}
libraries |= {"zoneinfo": "IANA time zone support"}
print(libraries)


# PEP 616 -- String methods to remove prefixes and suffixes
print("TestHook".removeprefix("Test"))
print("BaseTestCase".removeprefix("Test"))

print("MiscTests".removesuffix("Tests"))
print("TmpDirMixin".removesuffix("Tests"))
