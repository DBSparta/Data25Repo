from reptile import Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = False
        self.venom = None
        self.limbs = False


snek = Snake()

print(snek.cold_blooded)


