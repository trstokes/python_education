def outer(x):
    def inner(y):
        print(x + y)

    return inner

outer(5)(6)


def a(x):
    def b(x):
        print(x)

    return b

# a('b')('b')

def foo(x):
    def bar():
        nonlocal x
        print(x)
        x = 1

    print(x)
    return bar

foo(3)()