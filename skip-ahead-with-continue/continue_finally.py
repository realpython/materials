for number in range(2):
    try:
        print(f"Iteration {number}: start of try block")

        if number == 1:
            print(f"  Executing `continue` in iteration {number}...")
            continue

        print(f"  Normal flow in iteration {number}...")

    except Exception as e:
        print(f"Iteration {number}: Exception: {e}")

    finally:
        print(f"Iteration {number}: finally block")

    print(f"Iteration {number}: rest of loop body", end="\n\n")
