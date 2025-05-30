def verify_purchase(age, selection, restricted_products):
    if age < 21 and not selection.isdisjoint(restricted_products):
        print("Purchase denied: selection includes age-restricted products")
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
