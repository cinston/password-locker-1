from unittest import TestCase, main
from credentials import Credentials


class TestCredentials(TestCase):
    """
      Defines test cases for the credentials class behaviours.

      Args:
        TestCase: A class that helps create the test cases.
    """

    def setUp(self):
        """
          Method that runs before the test cases.
        """
        self.new_cred = Credentials('sam10105', 'samisbae')

    def tearDown(self):
        """
          Method that does clean up after each test has run.
        """
        Credentials.cred_list = []

    def test_init(self):
        """
          Test case to see if the objects are being initialized properly.
        """
        self.assertEqual(self.new_cred.username, 'sam10105')
        self.assertEqual(self.new_cred.password, 'samisbae')

    def test_store_existing_cred(self):
        """
          Test case to check whether credentials can be stored in cred_list.
        """
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list), 1)

    def test_store_multiple_cred(self):
        """
          Test case to check whether multiple credentials can be stored in cred_list.
        """
        self.new_cred.save_cred()
        test_cred = Credentials('samE', 'sam123FTW')
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list), 2)

    def test_display_cred(self):
        """
          Test case to check if the credentials can be displayed.
        """
        self.assertEqual(Credentials.display_cred(), Credentials.cred_list)


if __name__ == '__main__':
    main()
