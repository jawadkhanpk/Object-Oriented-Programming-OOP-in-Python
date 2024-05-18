# prettytable package version = 3.10.0
from prettytable import PrettyTable

my_prettytable = PrettyTable()
my_prettytable.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
my_prettytable.add_column("Type",["Electric", "Water", "Fire"])

# modifying object attributes
my_prettytable.align = 'l'

print(my_prettytable)