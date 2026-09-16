# Operators and Expressions in Python

This folder provides the code examples for the Real Python tutorial [Operators and Expressions in Python](https://realpython.com/python-operators-expressions/).

## Running the Examples

The tutorial presents its examples in the interactive REPL. Here, each section
of the tutorial has its own self-contained script that runs the same code in
the same order and prints the results. The examples only use the standard
library, so there's nothing to install. Run any of them with Python 3.14 or
later:

```sh
$ python arithmetic.py
```

| File                           | Tutorial section                                    |
| ------------------------------ | --------------------------------------------------- |
| `getting_started.py`           | Getting Started With Operators and Expressions      |
| `assignment.py`                | The Assignment Operator and Statements              |
| `arithmetic.py`                | Arithmetic Operators and Expressions in Python      |
| `comparison.py`                | Comparison Operators and Expressions in Python      |
| `comparison_integers.py`       | Comparison of Integer Values                        |
| `comparison_floats.py`         | Comparison of Floating-Point Values                 |
| `comparison_strings.py`        | Comparison of Strings                               |
| `comparison_sequences.py`      | Comparison of Lists and Tuples                      |
| `boolean_operands.py`          | Boolean Expressions Involving Boolean Operands      |
| `boolean_context.py`           | Evaluation of Regular Objects in a Boolean Context  |
| `boolean_other_operands.py`    | Boolean Expressions Involving Other Types of Operands |
| `short_circuit.py`             | Compound Logical Expressions and Short-Circuit Evaluation |
| `short_circuit_idioms.py`      | Idioms That Exploit Short-Circuit Evaluation        |
| `chained_comparisons.py`       | Compound vs Chained Expressions                     |
| `conditional_expressions.py`   | Conditional Expressions or the Ternary Operator     |
| `identity.py`                  | Identity Operators and Expressions in Python        |
| `membership.py`                | Membership Operators and Expressions in Python      |
| `concatenation_repetition.py`  | Concatenation and Repetition Operators and Expressions |
| `walrus.py`                    | The Walrus Operator and Assignment Expressions      |
| `bitwise.py`                   | Bitwise Operators and Expressions in Python         |
| `precedence.py`                | Operator Precedence in Python                       |
| `augmented_assignment.py`      | Augmented Assignment Operators and Expressions      |

A few of the tutorial's snippets can't live in a script: the bare `-`, `==`,
and `or` operators are a `SyntaxError`, and several snippets are syntax
sketches with placeholder names. Those are noted in comments where they
belong. Where the tutorial shows a traceback, the script catches the
exception and prints its message so that you can still see the error.
