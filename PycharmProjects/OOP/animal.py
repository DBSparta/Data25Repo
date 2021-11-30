class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print('inhale exhale')

    def eat(self):
        print('nom nom nom')

    def procreate(self):
        print('time to mate')
a = 1

# while number != 0:
#     x = [0, 0]
#     if number % 2 == 0:
#         x[0] += number
#         number = number -1
#     else:
#         x[1] += number
#         number = number -1


def f(a, b):
    x = a
    for i in range(0, int(len(x)/2)):
        if b == x[2 * i]:
            return True
    else:
        return False


a = [1, 2, 3, 4, 5]
print(f(a, 5))
print(int(len(a)/2))
print(a[4])
