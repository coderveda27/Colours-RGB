import a1_helpers

def warmup_part4() -> None:
    """Visualize an example colour row using pygame.

    This function illustrates the use of the helper function a1_helpers.show_colours_pygame
    that we have provided you. We encourage you to use that function to visualize your
    work on the various questions in this part of the assignment!
    """
    example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]

    a1_helpers.show_colours_pygame(example_colours)


###################################################################################################
# 1. Cropping colour rows
###################################################################################################
def crop_row(colour_row: list, start: int, num_colours: int) -> list:
    """Return a colour row containing the specified colours from the given colour_row.

    Notes:
    1. start is the index of the first colour to take from colour_row.
    2. num_colours specifies the number of colours to take from colour_row.
        If num_colours == 0, no colours are taken (and an empty list is returned)

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)
    - start >= 0
    - num_colours >= 0
    - start + num_colours <= len(colour_row)

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> crop_row(example_colours, 1, 2)  # Take two colours from example_colours starting at index 1
    [[1, 2, 3], [100, 100, 100]]
    """
    return [colour_row[i] for i in range(start, num_colours + start)]


def crop_row_border_single(colour_row: list) -> list:
    """Return a colour row with the colours from the given colour_row, except with the first and last colour removed.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)
    - len(colour_row) >= 2

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> crop_row_border_single(example_colours)
    [[1, 2, 3], [100, 100, 100], [181, 57, 173]]

    You may implement this function by using a list comprehension OR by calling crop_row
    with the appropriate arguments. (For extra practice, try both ways!)
    """
    return crop_row(colour_row, 1, len(colour_row) - 2)


def crop_row_border_multiple(colour_row: list, border_size: int) -> list:
    """Return a colour row with the colours from the given colour_row, except with
    the first and last border_size colours removed.

    Note: when border_size == 1, this function does the same thing as crop_row_border_single.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)
    - 1 <= border_size <= len(colour_row) // 2

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> crop_row_border_multiple(example_colours, 1)  # Remove the first and last colours
    [[1, 2, 3], [100, 100, 100], [181, 57, 173]]
    >>> crop_row_border_multiple(example_colours, 2)  # Remove the first 2 and last 2 colours
    [[100, 100, 100]]

    You may implement this function by using a list comprehension OR by calling crop_row
    with the appropriate arguments. (For extra practice, try both ways!)
    """
    return crop_row(colour_row, border_size, len(colour_row) - (border_size + border_size))


###################################################################################################
# 2. Changing colours (reds)
###################################################################################################
def remove_red_in_row(colour_row: list) -> list:
    """Return a new colour row consisting of the same colours as the given row, except each colour
    has its "red" value changed to 0.

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> remove_red_in_row(example_colours)
    [[0, 255, 200], [0, 2, 3], [0, 100, 100], [0, 57, 173], [0, 0, 197]]
    """
    return [[0] + [i[1]] + [i[2]] for i in colour_row]


def fade_red_in_row(colour_row: list) -> list:
    """Return a new colour row consisting of the same colours as the given row, except each colour
    has its "red" value multiplied by 0.25 and rounded to the nearest integer.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> fade_red_in_row(example_colours)
    [[0, 255, 200], [0, 2, 3], [25, 100, 100], [45, 57, 173], [8, 0, 197]]
    """
    return [[round(i[0] * 0.25)] + [i[1]] + [i[2]] for i in colour_row]


###################################################################################################
# 3. Changing colours (fade and blur)
###################################################################################################
def fade_row(colour_row: list) -> list:
    """Return a new colour row consisting of the colours in the given row, with each faded by an
    amount corresponding to its index.

    We perform a *fade* on the colour tuple at index i by multiplying each of its int values
    by (i / len(colour_row)) and then rounding to the nearest integer.
    So for example, if len(colour_row) == 5:

    - colour_row[0] has each of its colour values multipled by 0 / 5 = 0.0, so you always get [0, 0, 0]
    - colour_row[1] has each of its colour values multipled by 1 / 5 = 0.2 and then rounded
    - colour_row[4] has each of its colour values multiplied 4 / 5 = 0.8 and then rounded

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> fade_row(example_colours)
    [[0, 0, 0], [0, 0, 1], [40, 40, 40], [109, 34, 104], [26, 0, 158]]
    """
    return [[round(colour_row[i][0] * (i / len(colour_row)))] + [round(colour_row[i][1] * (i / len(colour_row)))]
            + [round(colour_row[i][2] * (i / len(colour_row)))] for i in range(0, len(colour_row))]


def blur_row(colour_row: list) -> list:
    """Return a new colour row consisting of the colours in the given row blurred together.

    We perform a *blur* on the colour tuple at index i by taking the average of the colour values
    at indexes i - 1, i, and i + 1, rounding to the nearest integer.

    For simplicity, we ignore the first and last colours in the row, and the returned list has length *2 less*
    than the original row.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)
    - len(colour_row) >= 2

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> blur_row(example_colours)
    [[34, 119, 101], [94, 53, 92], [105, 52, 157]]

    Hints:
        - Because you are dropping the first and last colours in the row, you can use a similar
          approach as crop_row_border_single.
        - You may find it helpful to first define a new function that takes three colours and
          returns their average, and then use that function here. But there are many other approaches
          you can take as well!
        - Even if you get stuck, you can move onto Part 5 and come back to this function later.
    """
    return average_colour([colour_row[i - 1] for i in range(1, len(colour_row) - 1)]) \
        + average_colour([colour_row[i] for i in range(1, len(colour_row) - 1)]) \
        + average_colour([colour_row[i + 1] for i in range(1, len(colour_row) - 1)])


def average_colour(colour_row: list) -> list:
    """
    This function takes a list of 3 colours values and returns their average rounded to the nearest integer

    >>> average_colour([[1, 2, 3], [100, 100, 100], [181, 57, 173]])
    [94, 53, 92]
    """
    return [[round((colour_row[0][i] + colour_row[1][i] + colour_row[2][i]) / 3) for i in range(0, len(colour_row))]]


###################################################################################################
# "Main block" (we'll discuss what this means in lecture)
###################################################################################################
if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['a1_helpers'],
        'max-line-length': 120
    })
