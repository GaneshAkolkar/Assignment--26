class UserAccount:
    def __init__(self, userid, balance):
        self.userid = userid
        self.balance = balance

    def __add__(self, other):
        new_user = UserAccount(self.userid + other.userid, self.balance + other.balance)
        return new_user

user1 = UserAccount("user1", 1000)
user2 = UserAccount("user2", 1500)
user3 = UserAccount("user3", 2000)

total_user = user1 + user2 + user3
print(f"Total User ID: {total_user.userid}, Total Balance: {total_user.balance}")
