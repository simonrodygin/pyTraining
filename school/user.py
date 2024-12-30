from credentials import Credentials

class User:
    user_amount = 0
    
    def __init__(self, name: str, credentials: Credentials):
        User.user_amount += 1
        print('new user was made')
        self.active = True
        self.name = name
        self.credentials = credentials
