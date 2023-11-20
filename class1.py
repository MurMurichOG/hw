class Hello:
    def __init__(self, name):
        self.name = name
class HI(Hello):
    def __str__(self):
        print(self.name)