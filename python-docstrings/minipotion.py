from classes_docstring import Potion


class MiniPotion(Potion):
    pass


help(MiniPotion)
print(MiniPotion.__doc__)
print(MiniPotion.brew.__doc__)
