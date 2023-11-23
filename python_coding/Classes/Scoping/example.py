def scope_test():
    def do_local():
        spam = 'local scope'
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal scope'
    def do_global():
        global spam
        spam = 'global scope'
    spam = 'test spam'
    do_local()
    print('After local assignment: ',spam)
    do_nonlocal()
    print('After non local assignment: ',spam)
    do_global()
    print('After global assignment: ',spam)

scope_test()
print('is global: ',spam)