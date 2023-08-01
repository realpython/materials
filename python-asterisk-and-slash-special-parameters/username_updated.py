def username(fn, ln, /, *, initial_last=True):
    if initial_last:
        return ln + fn[0]
    else:
        return fn[0] + ln


username("Frank", "Sinatra")
username("Frank", "Sinatra", initial_last=False)

# This would be invalid:
# username(fn="Frank", ln="Sinatra", initial_last=False)
