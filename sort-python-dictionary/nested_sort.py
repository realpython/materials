data = {
    193: {"name": "John", "age": 30, "skills": {"python": 8, "javascript": 7}},
    209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
    746: {"name": "Jane", "age": 58, "skills": {"javascript": 2, "python": 5}},
    109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
    984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
    765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
    598: {"name": "Sylvia", "age": 30, "skills": {"bash": 8, "java": 7}},
    483: {"name": "Anna", "age": 30, "skills": {"javascript": 10}},
    277: {
        "name": "Beatriz",
        "age": 30,
        "skills": {"python": 2, "javascript": 4},
    },
}


def getPython(item):
    skills = item[1]["skills"]

    return skills["python"] if "python" in skills else 0


print(sorted(data.items(), key=getPython, reverse=True))
