class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print(f"{exc_type  = }")
        print(f"{exc_value = }")
        print(f"{exc_tb    = }")


if __name__ == "__main__":
    with HelloContextManager() as hello:
        print(hello)

    print("Continue normally from here...")

    with HelloContextManager() as hello:
        hello[100]
