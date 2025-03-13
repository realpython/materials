import re

shopping_mess = "Apple  :::::3:Orange  |  2|||Lemon --1-Date   :: 10"
shopping_list = re.split(r"\s*[:|-]+\s*", shopping_mess)

print(shopping_list)
