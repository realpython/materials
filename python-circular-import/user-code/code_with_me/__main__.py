from interface import create_instance


def main():
    # Create an instance of ImplementationA
    implementation = create_instance('A')
    implementation.do_something()  # Output: Implementation A is doing something.

    # Create an instance of ImplementationB
    implementation = create_instance('B')
    implementation.do_something()  # Output: Implementation B is doing something.

if __name__ == "__main__":
    main()