# flake8: noqa

__generated_with = "0.11.0"

# %%
import marimo as mo

# %%
mo.md(
    r"""
    A quadratic equation is one of the form **$ax^2 + bx + c = 0$**, where a, b and c are constants, and a $\neq$ 0.

    You can solve it using the *quadratic formula*:

    $$x = \frac {-b \pm \sqrt{b^2 -4ac}} {2a}$$

    For example, suppose you wanted to solve: **$2x^2 - 3x - 2 = 0$**
    """
)

# %%
a = 2

# %%
import math

# %%
b = -3

# %%
c = -2

# %%
x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

# %%
x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

# %%
print(f"x = {x1} and {x2}.")