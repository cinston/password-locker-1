class Credentials:
    """
      Class that creates instances of credentials.
    """
    cred_list = []

    def __init__(self, username, password):
        """
          Defines properties for our objects.

          Args:
            username: new username.
            password: new password.
        """
        self.username = username
        self.password = password

    def save_cred(self):
        """
          Method that stores objects into cred_list.
        """
        self.cred_list.append(self)

    @classmethod
    def display_cred(cls):
        """
          Method that returns the cred_list list
        """
        return cls.cred_list
