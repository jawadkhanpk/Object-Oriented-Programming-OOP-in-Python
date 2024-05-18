from turtle import Turtle, Screen

# Constructing an object for Screen class, A Class is a template/blueprint for creating an object
# Class contains attributes and methods which can be accessed through object
# here my_screen is an object, and Screen() is a class which is imported form Turtle Library
my_screen_object = Screen()

# here 'canvheight' is the attribute of Turtle Class which is accessed using 'my_screen_object'
print(my_screen_object.canvheight)

# here exitonclick() is the method of a Turtle Class, which is accessed using 'my_screen_object'
my_screen_object.exitonclick()