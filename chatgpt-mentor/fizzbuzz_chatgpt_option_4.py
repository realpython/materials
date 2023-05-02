def fizzbuzz(n):
    mapping = {3: "fizz", 5: "buzz", 15: "fizz buzz"}
    for i in range(1, n + 1):
        output = ""
        for key in mapping:
            if i % key == 0:
                output += mapping[key]
        if output == "":
            output = i
        print(output)
