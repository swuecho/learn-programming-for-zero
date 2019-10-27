class Dual(object):
    def __init__(self, x, a=0):
        self.x = x
        self.a = a

    def __add__(self, other):
        return Dual(self.x + other.x, self.a + other.a)

    def __mul__(self, other):
        return Dual(self.x * other.x,
                    other.x * self.a + self.x * other.a)

    def __truediv__(self, other):
        return Dual(self.x / other.x,
                    (other.x * self.a - self.x * other.a)/other.x**2)


def f(x):
    return x*x


def babylonia(x, N=10):
    t = (Dual(1)+x)/Dual(2)
    for i in range(1, N):
        t = (t+x/t)/Dual(2)
    return t


if __name__ == "__main__":
    x = f(Dual(5, 1)).x
    a = f(Dual(5, 1)).a
    print(x, a)

    #print(babylonia(2, 10))
    x = babylonia(Dual(49, 1), 10).x
    a = babylonia(Dual(49, 1), 10).a
    print(x, a)
