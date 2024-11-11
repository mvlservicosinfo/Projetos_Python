class Execicio1:
    def __init__(self, num):
        self.num = num

    def executar(self):
            mult = -1
            fat = 1
            for i in range(self.num):
                print(fat * (i - self.num), end=" ")
                fat = fat * mult
