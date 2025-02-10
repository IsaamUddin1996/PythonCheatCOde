# merge dictionaries:
dict1 = {"name":"Joe"}
dict2 = {"age": 32,"name":"Sam"}
merged = {**dict1, **dict2}
print(merged)
dict1.update({"age": 32,"name":"Sam"})
print(dict1)
