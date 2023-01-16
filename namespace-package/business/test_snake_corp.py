from snake_corp import ordering, sales

print(ordering.get_product_by_id("2194"))

ordering.make_order("2194", 50)

print(sales.get_sales_by_product_id("2194"))
