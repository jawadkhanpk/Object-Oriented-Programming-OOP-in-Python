# Creating a Blank class
class User:
    # 'pass' keyword is used if there is nothing inside class or when class is expecting an indent
    pass


# constructing object for class
my_user1 = User()
my_user1.id = 34
my_user1.username = "jawadkhanpk"

print(f"{my_user1.id}\n{my_user1.username}")


my_user2 = User()
my_user2.userid= "56"
my_user2.username = "devadan"

print(f"{my_user2.id}\n{my_user2.username}")