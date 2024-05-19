class User:
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username
        self.followers = 0  # this is what if we want to set default value for all the users, there is no need of passing parameter in this case
        print("new user being created...")


# constructing object for class
my_user1 = User(34, "jawadkhanpk")
print(f"{my_user1.userid}\n {my_user1.username}\n")

my_user2 = User(56, "devadan")
print(f"{my_user2.userid}\n {my_user2.username}")

print(f"\nuser1 followers: {my_user1.followers}")
print(f"user2 followers: {my_user2.followers}")

# Output of a Program
# new user being created...
# 34
#  jawadkhanpk
#
# new user being created...
# 56
#  devadan
#
# user1 followers: 0
# user2 followers: 0