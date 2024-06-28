def evaluator(expression):
    numbers = [2, 3, 4, 5]
    n = len(numbers)
    return eval(expression, {}, {"numbers": numbers, "n": n})


print(evaluator("sum(numbers) / n + 100"))  # 3.5
