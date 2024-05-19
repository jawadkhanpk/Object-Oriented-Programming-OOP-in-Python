class User:
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):     # "self" keyword in method parameter is a way for us to refer to the object that's going to be created from User class inside the class blueprint.
        user.followers +=1
        self.following +=1


# constructing object for class
my_user1 = User(34, "jawadkhanpk")


my_user2 = User(56, "devadan")


# if my_user1 follows my_user2
my_user1.follow(my_user2)

print(f"user1 followers: {my_user1.followers}")
print(f"user1 following: {my_user1.following}")

print(f"user2 followers: {my_user2.followers}")
print(f"user2 following: {my_user2.following}")

# Output
# user1 followers: 0
# user1 following: 1
# user2 followers: 1
# user2 following: 0