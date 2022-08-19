try:
    raise ExceptionGroup(
        "group", [TypeError("str"), ValueError(654), TypeError("int")]
    )
except* ValueError as eg:
    print(f"Handling ValueErrors: {eg.exceptions}")
