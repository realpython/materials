class SortableDict(dict):
    def sort_by_keys(self, reverse=False):
        sorted_items = sorted(
            self.items(), key=lambda item: item[0], reverse=reverse
        )
        self.clear()
        self.update(sorted_items)

    def sort_by_values(self, reverse=False):
        sorted_items = sorted(
            self.items(), key=lambda item: item[1], reverse=reverse
        )
        self.clear()
        self.update(sorted_items)


students = SortableDict(
    {
        "Alice": 89.5,
        "Bob": 76.0,
        "Charlie": 92.3,
        "Diana": 84.7,
        "Ethan": 88.9,
        "Fiona": 95.6,
        "George": 73.4,
        "Hannah": 81.2,
    }
)

print(id(students))
students.sort_by_keys()
print(students)
students.sort_by_values(reverse=True)
print(students)
print(id(students))
