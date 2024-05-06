import pickle

import plus


def main():
    function_raw = pickle.dumps(plus.create_plus)
    function = pickle.loads(function_raw)
    print(function_raw)
    print(function)
    print(f"{function(3)(2) = }")


if __name__ == "__main__":
    main()
