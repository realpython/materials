person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 35,
    "spouse": "Jane",
    "children": ["Ralph", "Betty", "Bob"],
    "pets": {"dog": "Frieda", "cat": "Sox"},
}

print(person["children"][0])
print(person["children"][2])
print(person["pets"]["dog"])

person = {}
person["first_name"] = "John"
person["last_name"] = "Doe"
person["age"] = 35
person["spouse"] = "Jane"
person["children"] = ["Ralph", "Betty", "Bob"]
person["pets"] = {"dog": "Frieda", "cat": "Sox"}
print(person)
