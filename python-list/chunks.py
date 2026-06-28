from typing import Any, List


def split_list(list_object: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split a list into smaller chunks of a given size.

    Args:
        list_object: The list to split.
        chunk_size: The size of each chunk (must be a positive integer).

    Returns:
        A list of sublists, each with at most `chunk_size` elements.

    Raises:
        ValueError: If chunk_size is less than or equal to zero.

    Example:
        >>> split_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    return [
        list_object[start : start + chunk_size]
        for start in range(0, len(list_object), chunk_size)
    ]
