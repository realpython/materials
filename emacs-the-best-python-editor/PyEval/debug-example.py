"""
Example code for debugging PyEval
"""

from pyeval_expression import Expression

expr = Expression("53 * -2 + 4")
expr.parse()
print(expr.result())
