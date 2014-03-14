def file_iterator(filename):
    with open(filename) as fd:
        for line in fd:
            yield line.strip()


def variadic_addition(*args):
    return sum(args)


def variadic_multiplication(*args):
    return reduce(lambda acc, i: acc * i, args)
