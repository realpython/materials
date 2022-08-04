from timeit import timeit

dict_to_order = {
    1: "requests",
    2: "pip",
    3: "jinja",
    4: "setuptools",
    5: "pandas",
    6: "numpy",
    7: "black",
    8: "pillow",
    9: "pyparsing",
    10: "boto3",
    11: "botocore",
    12: "urllib3",
    13: "s3transfer",
    14: "six",
    15: "python-dateutil",
    16: "pyyaml",
    17: "idna",
    18: "certifi",
    19: "typing-extensions",
    20: "charset-normalizer",
    21: "awscli",
    22: "wheel",
    23: "rsa",
}

sorted_with_lambda = "sorted(dict_to_order.items(), key=lambda item: item[1])"
sorted_with_itemgetter = "sorted(dict_to_order.items(), key=itemgetter(1))"

sorted_with_lambda_time = timeit(stmt=sorted_with_lambda, globals=globals())
sorted_with_itemgetter_time = timeit(
    stmt=sorted_with_itemgetter,
    setup="from operator import itemgetter",
    globals=globals(),
)

print(
    f"""\
{sorted_with_lambda_time=:.2f} seconds
{sorted_with_itemgetter_time=:.2f} seconds
itemgetter is {(
    sorted_with_lambda_time / sorted_with_itemgetter_time
):.2f} times faster"""
)
