class Base:
    attr = 100


class X(Base):
    pass


class Y(Base):
    pass


class Z(Base):
    pass


print(X.attr)
print(Y.attr)
print(Z.attr)
