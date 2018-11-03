class User:
    """
      A class that generates new instances of users.
    """

    def __init__(self, first_name, last_name, username, password):
        """
          Defines properties for our objects.

          Args:
            first_name: New user first name.
            last_name: New user last name.
            username: New user username.
            password: New user password.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
