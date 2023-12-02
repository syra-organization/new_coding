# its like types in TS

def foo(num: str, eggs: str, iseated: bool) -> str:
    print('Annotations', foo.__annotations__)
    print('Arguments', num, eggs, iseated)
    return eggs


value = foo(2, 'eggs', True)
print(value)
