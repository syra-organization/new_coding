# Duck typing 

class Laptop:
    def __init__(self) -> None:
        pass

    def code(self,ide):
        ide.execute()

class MyIDE:
    def __init__(self) -> None:
        pass

    def execute(self):
        print('Spell check')
        print('Compiling')
        print('Running')

class Pycharm:
    def __init__(self) -> None:
        pass

    def execute(self):
        print('Compiling')
        print('Running')

#ide = Pycharm()

ide = MyIDE()

lap1 = Laptop()
lap1.code(ide)