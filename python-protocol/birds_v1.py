class Duck:
    def quack(self):
        return "The duck is quacking!"


def make_it_quack(duck: Duck) -> str:
    return duck.quack()


class Person:
    def quack(self):
        return "The person is imitating a duck quacking!"


print(make_it_quack(Duck()))
# print(make_it_quack(Person()))
