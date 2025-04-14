def verify_purchase(age, selection, restricted_products):
    if age < 21:
        if not selection.isdisjoint(restricted_products):
            print("Purchase denied: products restricted to underage users")
        else:
            print("Purchase approved")
    else:
        print("Purchase approved")


verify_purchase(
    age=18,
    selection={"milk", "bread", "beer"},
    restricted_products={"alcohol", "beer", "cigarettes"},
)
verify_purchase(
    age=18,
    selection={"milk", "bread"},
    restricted_products={"alcohol", "beer", "cigarettes"},
)
verify_purchase(
    age=35,
    selection={"milk", "bread", "beer"},
    restricted_products={"alcohol", "beer", "cigarettes"},
)
