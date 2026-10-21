"""Statements that grow too long to read comfortably on one line.

Code from the "Line Continuation" section of the tutorial: these are the
"before" examples that motivate implicit and explicit line continuation.
The excessive line lengths are deliberate.

The tutorial also shows an unterminated statement that raises a
SyntaxError. That block is not reproduced here because it cannot run.
"""

# fmt: off
person1_age = 42
person2_age = 16
person3_age = 71

someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)
print(someone_is_of_working_age)

a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
print(a)
# fmt: on
