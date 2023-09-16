class UserAccount:
    def __init__(self, userid, balance):
        self.userid = userid
        self.balance = balance

    def __str__(self):
        return f"User ID: {self.userid}, Balance: {self.balance}"

user = UserAccount("user1", 1000)
print(user)
