# Reviewing the sorted() function by sorting a list
numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
sorted(numbers)
words = ["aa", "ab", "ac", "ba", "cb", "ca"]
sorted(words)


def select_second_character(word):  # Sort key
    return word[1]


sorted(words, key=select_second_character)

# Feeding dictionary directly into sorted() function
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
sorted(people)  # Returns list of sorted keys (values gone)

# Getting dictionary views
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
people.items()

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
view = people.items()
people[2] = "Elvis"
print(view)  # View has been updated

# Feeding dictionary view directly into sorted() function
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
sorted(people.items())  # Sorts by key

# Using a sort key when sorting dictionary views
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}


def value_getter(item):  # Sort key
    return item[1]


sorted(people.items(), key=value_getter)
sorted(people.items(), key=lambda item: item[1])  # Sort key as lambda function


# Building a dictionary from the list returned from the sorted() function
sorted_people = sorted(people.items(), key=lambda item: item[1])

sorted_people_dict = {}  # Using a for loop
for key, value in sorted_people:
    sorted_people_dict[key] = value

sorted_people = sorted(people.items(), key=lambda item: item[1])
sorted_people_dict = dict(sorted_people)  # dictionary constructor

sorted_people_dict = {  # dictionary comprehension that swaps keys and values
    value: key
    for key, value in sorted(people.items(), key=lambda item: item[1])
}
