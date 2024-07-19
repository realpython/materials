class QuackingThing:
    def quack(self):
        raise NotImplementedError("Subclasses must implement this method")


class Duck(QuackingThing):
    def quack(self):
        return "The duck is quacking!"


class Person(QuackingThing):
    def quack(self):
        return "The person is imitating a duck quacking!"


def make_it_quack(duck: QuackingThing) -> str:
    return duck.quack()


print(make_it_quack(Duck()))
print(make_it_quack(Person()))
