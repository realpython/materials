def outer_func(outer_arg):
    local_var = "Outer local variable"

    def closure():
        print(outer_arg)
        print(local_var)
        print(another_local_var)

    another_local_var = "Another outer local variable"

    return closure
