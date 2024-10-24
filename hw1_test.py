import data
import hw1
import unittest

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel(self):
        string = "My name is Camille"
        result = hw1.vowel_count(string)
        expected = 6
        self.assertEqual(expected, result)

    def test_vowel2(self):
        string = "I love food"
        result = hw1.vowel_count(string)
        expected = 5
        self.assertEqual(expected, result)

    # Part 2
    def test_list(self):
        list1 = [[3, 4], [3], [4, 5, 6], [10, 19]]
        result = hw1.short_lists(list1)
        expected = [[3,4],[10,19]]
        self.assertEqual(expected, result)

    def test_list2(self):
        list1 = [[3], [4, 5, 6], [1, 21], [], [49]]
        result = hw1.short_lists(list1)
        expected = [[1,21]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending(self):
        list1 = [[1, 3], [2, 1], [3], [7, 2]]
        result = hw1.ascending_pairs(list1)
        expected = [[1,3], [1,2], [3], [2,7]]
        self.assertEqual(expected, result)

    def test_ascending2(self):
        list1 = [[4, 3], [21, 1], [3], [49,37]]
        result = hw1.ascending_pairs(list1)
        expected = [[3,4], [1,21], [3], [37,49]]
        self.assertEqual(expected, result)

    # Part 4
    def test_price(self):
        price1 = data.Price(5, 50)
        price2 = data.Price(3, 25)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(8,75)
        self.assertEqual(expected, result)

    def test_price2(self):
        price1 = data.Price(7, 80)
        price2 = data.Price(4, 20)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(12,0)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle(self):
        rect1 = data.Rectangle(data.Point(1,1), data.Point(4, 3))
        result = hw1.rectangle_area(rect1)
        expected = 6.0
        self.assertEqual(expected, result)

    def test_rectangle2(self):
        rect2 = data.Rectangle(data.Point(3,3), data.Point(4, 4))
        result = hw1.rectangle_area(rect2)
        expected = 1.0
        self.assertEqual(expected, result)

    # Part 6
    def test_author(self):
        book1 = data.Book("Book 1", "Camille")
        book2 = data.Book("Book 2", "Rapunzel")
        book3 = data.Book("Book 3", "Rapunzel")
        book4 = data.Book("Book 4", "Camille")
        books = [book1, book2, book3, book4]
        result = hw1.books_by_author("Camille", books)
        expected = [book1,book4]
        self.assertEqual(expected, result)

    def test_author2(self):
        book1 = data.Book("Book 1", "Camille")
        book2 = data.Book("Book 2", "Rapunzel")
        book3 = data.Book("Book 3", "Rapunzel")
        book4 = data.Book("Book 4", "Camille")
        books = [book1, book2, book3, book4]
        result = hw1.books_by_author("Rapunzel", books)
        expected = [book2,book3]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle(self):
        rect1 = data.Rectangle(data.Point(0, 0), data.Point(2, 2))
        result = hw1.circle_bound(rect1)
        expected = data.Circle(data.Point(1.0,1.0),1)
        self.assertEqual(result, expected)

    def test_circle2(self):
        rect1 = data.Rectangle(data.Point(1, 1), data.Point(5, 4))
        result = hw1.circle_bound(rect1)
        expected = data.Circle(data.Point(3.0,2.5),2)
        self.assertEqual(result,expected)

    # Part 8
    def test_employee(self):
        employee1 = data.Employee("Camille", 50)
        employee2 = data.Employee("Diego", 40)
        employee3 = data.Employee("Charlie", 60)
        employees = [employee1, employee2, employee3]
        result = hw1.below_pay_average(employees)
        expected = ["Diego"]
        self.assertEqual(result,expected)

    def test_employee2(self):
        employee1 = data.Employee("Kate", 98)
        employee2 = data.Employee("Kloe", 100)
        employee3 = data.Employee("Joy", 63)
        employees = [employee1, employee2, employee3]
        result = hw1.below_pay_average(employees)
        expected = ["Joy"]
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()
