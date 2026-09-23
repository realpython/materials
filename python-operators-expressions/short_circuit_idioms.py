# Avoiding an exception
a = 3
b = 1

print((b / a) > 0)

a = 0
b = 1

try:
    print((b / a) > 0)
except ZeroDivisionError as error:
    print(error)

print(a != 0 and (b / a) > 0)


def is_divisible(a, b):
    return b != 0 and a % b == 0


# Providing a default value
country = "Canada"
default_country = "United States"

print(country or default_country)

country = ""
print(country or default_country)

# Skipping a costly operation. The tutorial shows these two idioms as
# sketches with placeholder names, so they aren't runnable as they stand:
#     data_is_clean or clean_data(data)
#     data_is_updated and process_data(data)
