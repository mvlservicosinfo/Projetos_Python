class Fatorial:
    def __init__(self, x):
        self.x =x

    def fatorial(self):
        result = 1
        for i in range(self.x):
            result *= (self.x-i)
        return result


