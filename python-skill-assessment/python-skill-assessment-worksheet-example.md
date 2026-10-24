# Python Skill Assessment Worksheet (Filled-In Example)

This is an example of a finished worksheet. The ratings and notes are made up. Use the blank worksheet for your own.

Rate each statement from 1 to 4:

| Rating | Meaning |
|--------|---------|
| 1 | I can't do this yet. |
| 2 | I've seen it, but I need to look it up. |
| 3 | I can do it, but I'm not sure I could teach it. |
| 4 | I can do it and explain it to someone else. |

Rate what you can do without looking anything up. For a statement with several skills, rate your weakest one.

The "Quiz question" column names the question in the Real Python [Python Skill Test](https://realpython.com/quizzes/python-skill-test/) that covers the same topic, so you can compare your rating with your result.

## Part 1: Rate Yourself Against Each Level

### Novice (Quiz score 0-3)

| I can... | Rating (1-4) | Quiz question | Notes |
|----------|--------------|---------------|-------|
| display values with `print()`. | 4 | Using print() | Daily. |
| define a function with `def`, pass arguments, and return a value. | 4 | Define a Function |  |
| install a package from PyPI with `python -m pip install`, ideally inside a virtual environment. | 3 | Installing Packages | Forget `-m` sometimes. |
| explain that a `for` loop variable takes each element from an iterable, such as a string or a list. | 4 | Loop Anatomy |  |
| use variables, operators, `if` statements, and basic built-in types (numbers, strings, lists). | 4 | Beyond the quiz |  |

### Intermediate (Quiz score 4-7)

| I can... | Rating (1-4) | Quiz question | Notes |
|----------|--------------|---------------|-------|
| tell mutable types (`list`) from immutable ones (`tuple`, `str`, `frozenset`). | 3 | Mutable Objects | Never used `frozenset`. |
| explain that dictionary keys must be hashable and that insertion order is kept since Python 3.7. | 3 | Dictionary Facts | Hashable: fuzzy. |
| read and write list comprehensions, including an `if` filter, and rewrite them as a `for` loop. | 4 | Understanding List Comprehensions | Nested ones slow me down. |
| use the standard library's common modules, such as `pathlib`, `collections`, and `json`, before reaching for third-party packages. | 3 | Beyond the quiz |  |

### Proficient (Quiz score 8-11)

| I can... | Rating (1-4) | Quiz question | Notes |
|----------|--------------|---------------|-------|
| explain what problem the `with` statement solves and why files close even when an exception occurs. | 2 | The With Statement | Use it, can't explain it. |
| recognize dunder methods such as `.__init__()` and `.__iadd__()` and say when Python calls them. | 2 | Spot the Dunder | Only `.__init__()`. |
| write a generator function with `yield` and explain why it's lazy. | 1 | Writing a Simple Generator | Never wrote one. |
| write and apply decorators, and explain how iterators and iterables work. | 2 | Beyond the quiz |  |

### Expert (Quiz score 12)

| I can... | Rating (1-4) | Quiz question | Notes |
|----------|--------------|---------------|-------|
| predict attribute lookup when data descriptors, non-data descriptors, and instance attributes compete. | 1 | Descriptor Precedence in Practice | New to me. |
| trace the C3 method resolution order and predict the output of cooperative `super()` calls. | 1 | Cooperative super() and the C3 MRO | Single inheritance only. |
| explain what a metaclass does, and write basic `async` code with `asyncio`. | 1 | Beyond the quiz |  |

## Part 2: Reconcile Your Self-Rating With the Quiz

Average your ratings for each level, including the _Beyond the quiz_ row, take the quiz, and then fill in the quiz columns. The quiz reports one overall result, so use the explanations for each question you missed to fill in the per-level column.

| Level | Your average rating | Quiz questions missed | Gap (rating vs. result) |
|-------|---------------------|-----------------------|-------------------------|
| Novice | 3.8 | 0 | None |
| Intermediate | 3.3 | 1 (Dictionary Facts) | One miss: a hint, so recheck hashable keys |
| Proficient | 1.8 | 2 (Spot the Dunder, Writing a Simple Generator) | Low rating, two of three missed: matches |
| Expert | 1.0 | 2 (both) | Low rating, both missed: matches |

**Overall quiz result:** Intermediate (7 of 12 correct)

**Self-rated level** (the highest level whose average, and every average below it, is 3 or more, or _Not yet Novice_ if your Novice average is below 3): Intermediate

**Do they match?** Yes. Next step: Proficient.

## Part 3: Turn Your Weakest Area Into a Study Plan

| Question | Your answer |
|----------|-------------|
| My weakest area (the lowest-level miss that your check confirmed, or your lowest-rated statement at the lowest level) | Dictionary Facts: why keys must be hashable |
| Why it matters for my goals | My scripts group records in dictionaries keyed by tuples |
| One resource I'll use | [Dictionaries in Python](https://realpython.com/python-dicts/) |
| What I'll do with it this week | Try a list as a key, read the error, and explain hashability in my notes |
| Hours I can set aside per week | 3 |
| Date I'll retake the quiz | Four weeks from today |
