class User:
    """
      A class that generates new instances of users.
    """

    user_list = []

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

    def save_user(self):
        """
          Method that saves objects to user_list.
        """
        self.user_list.append(self)

    @classmethod
    def user_exists(cls, logged_user):
        """
        Method that checks is a user exists from the user list

        args:
            logged_user:username to search if the user exists

        returns:
            boolean:true or false depending on the condition
        """
        for user in cls.user_list:
            if user.username == logged_user:
                return True

        return False
