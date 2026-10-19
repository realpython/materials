"""The same function documented in four common docstring formats.

Compare the output of help() on each function to see how the Google,
reStructuredText, NumPy/SciPy, and Epytext formats look.
"""

import pandas as pd


def get_spreadsheet_cols_google(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Args:
        file_loc (str): The file location of the spreadsheet
        print_cols (bool): A flag used to print the columns to the console
            (default is False)

    Returns:
        list: a list of strings representing the header columns
    """

    if file_loc.lower().endswith(".csv"):
        file_data = pd.read_csv(file_loc)
    else:
        file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers


def get_spreadsheet_cols_rest(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    :param file_loc: The file location of the spreadsheet
    :type file_loc: str
    :param print_cols: A flag used to print the columns to the console
        (default is False)
    :type print_cols: bool
    :returns: a list of strings representing the header columns
    :rtype: list
    """

    if file_loc.lower().endswith(".csv"):
        file_data = pd.read_csv(file_loc)
    else:
        file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers


def get_spreadsheet_cols_numpy(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is False)

    Returns
    -------
    list
        a list of strings representing the header columns
    """

    if file_loc.lower().endswith(".csv"):
        file_data = pd.read_csv(file_loc)
    else:
        file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers


def get_spreadsheet_cols_epytext(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    @type file_loc: str
    @param file_loc: The file location of the spreadsheet
    @type print_cols: bool
    @param print_cols: A flag used to print the columns to the console
        (default is False)
    @rtype: list
    @returns: a list of strings representing the header columns
    """

    if file_loc.lower().endswith(".csv"):
        file_data = pd.read_csv(file_loc)
    else:
        file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers


if __name__ == "__main__":
    for func in (
        get_spreadsheet_cols_google,
        get_spreadsheet_cols_rest,
        get_spreadsheet_cols_numpy,
        get_spreadsheet_cols_epytext,
    ):
        print(f"--- {func.__name__} ---")
        print(func.__doc__)
