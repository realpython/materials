def push_and_pop[T](elements: list[T], element: T) -> T:
    elements.append(element)
    return elements.pop(0)
