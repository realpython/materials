data = {
    193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
    209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
    746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
    109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
    984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
    765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
    598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
    483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
    277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
}


def get_python(item):
    skills = item[1]["skills"]
    if "python" in skills:
        return skills["python"]
    else:
        # Return value that is equivalent to having no Python skill
        return 0


print(sorted(data.items(), key=get_python, reverse=True))

# Doing the same thing with lambda function and conditional expression
print(
    sorted(
        data.items(),
        key=lambda item: item[1]["skills"]["python"]
        if "python" in item[1]["skills"]
        else 0,
        reverse=True,
    )
)
