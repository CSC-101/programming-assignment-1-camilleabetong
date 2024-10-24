import data
import math

# Write your functions for each part in the space below.

# Part 1
def vowel_count(string: str) -> int:
    """
    Purpose: Count the number of vowels in the given string.

    Input: string
    Output: integer

    Parameters:
    string (str): The string in which to count vowels.

    Returns:
    int: The total number of vowels (a, e, i, o, u) in the input string.
    """
    vowels = "aeiouAEIOU"
    count = sum(1 for characters in string if characters in vowels)
    return count

# Part 2
def short_lists(lists) -> list:
    """
    Extracts sub-lists of length 2 from the given list of lists.

    Input: list
    Output: list

    Parameters:
    input_lists (List[List[int]]): A list of lists containing integers.

    Returns:
    List[List[int]]: A new list containing only the sub-lists of length 2.
    """
    return [sublist for sublist in lists if len(sublist) == 2]

# Part 3
def ascending_pairs(lists: list) -> list:
    """
    Purpose:
    Sorts nested lists of length 2 in non-descending order within the given list of lists.

    Input: list
    Output: list

    Parameters:
    input_lists (List[List[int]]): A list of lists containing integers.

    Returns:
    List[List[int]]: A new list where nested lists of length 2 are sorted, and others remain unchanged.
    """
    return [sorted(sublist) if len(sublist) == 2 else sublist for sublist in lists]

# Part 4
def add_prices(price1: data.Price, price2: data.Price) -> data.Price:
    """
    Sums two Price objects and returns a new Price object with valid cents.

    Input: price point
    Output: string

    Parameters:
    price1 (Price): The first price object.
    price2 (Price): The second price object.

    Returns:
    Price: A new Price object representing the sum of the two input prices.
    """
    total_cents = price1.cents + price2.cents
    total_dollars = price1.dollars + price2.dollars + total_cents // 100
    total_cents = total_cents % 100
    return data.Price(total_dollars, total_cents)

# Part 5
def rectangle_area(rect: data.Rectangle) -> float:
    """
    Purpose:
    Computes the area of the given rectangle.

    Input: rectangle point
    Output: integer

    Parameters:
    rect (Rectangle): A Rectangle object representing the rectangle.

    Returns:
    int: The area of the rectangle calculated as width * height.
    """
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.bottom_right.y - rect.top_left.y

    # Return the area (width * height)
    return width * height

# Part 6
def books_by_author(author_name: str, books: list) -> list:
    """
    Purpose:
    Filters books by the specified author.

    Input: string & list
    Output: list

    Parameters:
    author_name (str): The name of the author to filter by.
    books (List[Book]): A list of Book objects.

    Returns:
    List[Book]: A list of books written by the specified author.
    """
    sample_book = data.Book("", author_name)

    # Filter the list using __eq__
    return [book for book in books if book == sample_book]

# Part 7
def circle_bound(rect: data.Rectangle) -> data.Circle:
    """
    Purpose:
    Computes the bounding circle for the given rectangle.

    Input: rectangle points
    Output: circle points

    Parameters:
    rect (Rectangle): A Rectangle object representing the rectangle.

    Returns:
    Circle: A Circle object representing the smallest circle that encloses the rectangle.
    """
    # Calculate the center of the rectangle
    center_x = (rect.top_left.x + rect.bottom_right.x) / 2
    center_y = (rect.top_left.y + rect.bottom_right.y) / 2
    center = data.Point(center_x, center_y)

    # Calculate the radius as the distance from the center to one of the corners
    corner_x = rect.top_left.x
    corner_y = rect.top_left.y
    radius = int(math.sqrt((center_x - corner_x) ** 2 + (center_y - corner_y) ** 2))

    return data.Circle(center, radius)

# Part 8
def below_pay_average(employees: list) -> list:
    """
    Purpose:
    Computes the names of employees being paid less than the average pay.

    Input: list
    Output: list

    Parameters:
    employees (List[Employee]): A list of Employee objects.

    Returns:
    List[str]: A list of names of employees paid below the average pay rate.
    """
    if not employees:
        return []

    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)

    return [employee.name for employee in employees if employee.pay_rate < average_pay]

