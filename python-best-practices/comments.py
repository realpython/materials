# Avoid this:
# def find_index(sorted_items, target):
#     # Set left index
#     left = 0
#     # Set right index
#     right = len(sorted_items) - 1
#     # Loop while left is less than right
#     while left <= right:
#         # Compute middle
#         mid = (left + right) // 2
#         # Check if equal
#         if sorted_items[mid] == target:
#             # Return mid
#             return mid
#         # Check if less than target
#         elif sorted_items[mid] < target:
#             # Move left up
#             left = mid + 1
#         else:
#             # Move right down
#             right = mid - 1
#     # Return -1 if not found
#     return -1


# Favor this:
def find_index(sorted_items, target):
    """Return the index of target in sorted_items, or -1 if not found."""
    left = 0
    right = len(sorted_items) - 1

    while left <= right:
        mid = (left + right) // 2
        value = sorted_items[mid]

        if value == target:
            return mid

        # If target is larger, you can safely ignore the left half
        if value < target:
            left = mid + 1
        # Otherwise, target must be in the left half (if present)
        else:
            right = mid - 1

    return -1
