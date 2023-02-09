with open("hello.txt", mode="r") as hello:
    print(f"File object: {hello}")
    print(f"Memory address: {id(hello)}")
    print("File content:")
    for line in hello:
        print("> ", line)
