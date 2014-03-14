def conditional(obj, condition):
    if condition == 'a':
        obj.foo()
    elif condition == 'b':
        obj.bar()
    elif condition == 'c':
        obj.baz(True)
    else:
        obj.fiz()
