def add_product(item, inventory=[]):
    inventory.append(item)
    return inventory


print(add_product("apple"))
print(add_product("banana"))
