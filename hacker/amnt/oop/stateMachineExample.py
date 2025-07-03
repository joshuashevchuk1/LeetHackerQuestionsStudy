from enum import Enum

class State(Enum):
    LOGGED_OUT = 0
    LOGGED_IN = 1

class APMStateMachine:
    def __init__(self):
        self.state = State.LOGGED_OUT
        self.balance = 1000
        self.user = None

    def _logged_out(self):
        if self.state == State.LOGGED_OUT:
            return True
        return False

    def _logged_in(self):
        if self.state == State.LOGGED_IN:
            return True
        return False

    def login(self, user):
        if self._logged_out():
            self.state = State.LOGGED_IN
            self.user = user
        else:
            print("logged in")

    def logout(self):
        if self._logged_in():
            self.user = None
            self.state = State.LOGGED_OUT
        else:
            print("logged out")

    def check_balance(self):
        if self._logged_in():
            print(self.balance)
        else:
            raise AuthError()

    def deposit(self, amount):
        if self._logged_in():
           self.balance += amount
        else:
            raise AuthError()

    def withdraw(self, amount):
        if self._logged_in():
           self.balance -= amount
        else:
            raise AuthError()

class AuthError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Unauthorized"