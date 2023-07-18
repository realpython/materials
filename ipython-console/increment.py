def salary_increment(salary):
    """Calculate the new salary after applying an increment.

    Args:
        salary (int): The current salary.

    Returns:
        str: A string indicating the new salary after increment.
    """
    increment = salary / 10
    new_salary = increment + salary
    return f"Your New Salary is: {new_salary}"
