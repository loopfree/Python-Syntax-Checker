class ExampleClass:
    def __init__(self):
        pass
class Exam(ExampleClass):
    def __init__(self, boo):
        if not boo:
            raise ValueError
        pass