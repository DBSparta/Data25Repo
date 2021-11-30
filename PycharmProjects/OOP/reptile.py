from animal import Animal


class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.ectotherm = True
        self.__heart_chamber = [3, 4]
        self.eggs = True

    def __seek_heat(self):
        print('Wheres the sun')

    def use_venom(self):
        print('toxic')

    def attract_mate_through_scent(self):
        print('xd')


