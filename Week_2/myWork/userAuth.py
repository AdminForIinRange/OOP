class userAuth:
    def __init__(self, username, email, authToken, sessionToken, success, error):
        self.username = username
        self.email = email
        self.authToken = authToken
        self.sessionToken = sessionToken
        self.provider = "google"
        self.success = success
        self.error = error



    def __str__(self):
        # todo: refactor to return a string instead of printing
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Auth Token: {self.authToken}")
        print(f"Session Token: {self.sessionToken}")
        print(f"Provider: {self.provider}")
        print(f"Success: {self.success}")
        print(f"Error: {self.error}")


newUserAUth = userAuth("test", "test", "test", "test", "test", "test")

print(newUserAUth)

