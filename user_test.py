from unittest import TestCase, main
from user import User


class TestUser(TestCase):
    """
      Defines test cases for the user class behaviours.

      Args:
        TestCase: A class that helps create the test cases.
    """

    def setUp(self):
        """
          Method to run before the test cases.
        """
        self.new_user = User('Sam', 'Kasyoki', 'sam10105', 'samisbae')

    def test_init(self):
        """
          Test case to see if the object is being initialized properly.
        """
        self.assertEqual(self.new_user.first_name, 'Sam')
        self.assertEqual(self.new_user.last_name, 'Kasyoki')
        self.assertEqual(self.new_user.username, 'sam10105')
        self.assertEqual(self.new_user.password, 'samisbae')


if __name__ == '__main__':
    main()
