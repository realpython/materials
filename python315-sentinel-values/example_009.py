# Both calls intentionally fail. Catch each error so you can see both.
try:
    sentinel("UNSET", "<unset>")
except TypeError as error:
    print(f"Expected TypeError: {error}")

try:
    sentinel(name="UNSET")
except TypeError as error:
    print(f"Expected TypeError: {error}")
