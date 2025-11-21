encoded_text = b"d\xe9j\xe0 vu"

print(f"{encoded_text.decode("utf-8", errors="ignore") = }")
print(f"{encoded_text.decode("utf-8", errors="replace") = }")
print(f"{encoded_text.decode("utf-8", errors="backslashreplace") = }")
print(f"{encoded_text.decode('utf-8')}")
