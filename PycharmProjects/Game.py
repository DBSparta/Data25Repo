from random import randint


class Character:
    def __init__(self, name, strength, magic, vitality):
        self.name = name
        self.strength = strength
        self.magic = magic
        self.vitality = vitality
        self.health_max = vitality * 5
        self.health = self.health_max


class Player(Character):
    def __init__(self, name, strength, magic, vitality, gender, race):
        super().__init__(name, strength, magic, vitality)
        self.gender = gender
        self.state = 'normal'
        self.race = race

    def quit(self):
        print('Player has quit the game')
        self.health = 0

    def help(self):
        print(Commands.keys())

    def stab(self):
        damage = randint(5 + self.strength, 5 + self.strength * 2)
        e1.health -= damage
        if e1.health <= 0:
            print("%s's stab kills Shade" % self.name)
        else:
            print('%s deals %s damage to Shade' % (self.name, damage))
            e1.attack(p)

    def fireball(self):fireb
        damage = randint(self.magic, self.magic * 2)
        e1.health -= damage
        if e1.health <= 0:
            print("%s's fireball kills Shade" % self.name)
        else:
            print('%s deals %s damage to Shade' % (self.name, damage))
            e1.attack(p)

    def heal(self):
        healing = randint(self.magic, self.magic * 2)
        if self.health + healing >= self.health_max:
            self.health = self.health_max
            print('%s heals themself to %s' % (self.name, self.health))
            e1.attack(p)
        else:
            self.health += healing
            print('%s heals themself to %s' % (self.name, self.health))
            e1.attack(p)

    def status(self):
        print("%s's health: %d/%d" % (self.name, self.health, self.health_max))

    def rest(self):
        if self.state != 'normal':
            print("%s can't rest now" % self.name)
        else:
            if self.health < self.health_max:
                if self.health < self.health + self.health_max * .35:
                    self.health += self.health_max * .35
                else:
                    self.health = self.health_max
            else:
                print("%s's heath is already full")

    def escape(self, enemy):
        if self.state != "Combat":
            print("%s is not in combat" % self.name)
        else:
            if randint(1, self.health) > randint(1, enemy.health):
                print("s got away safely")
            else:
                print("s couldn't escape")
                e1.attack(p)

    def encounter(self):
        if self.state != 'normal':
            print('%s is already in combat' % self.name)
        else:
            self.enemy = e1
            print('%s encounters %s' % (self.name, e1.name))
            self.state = 'Combat'


class Enemy(Character):
    def __init__(self, name, strength, magic, vitality):
        super().__init__(name, strength, magic, vitality)

    def attack(self, enemy):
        damage = randint(self.strength, self.strength * 2)
        enemy.health -= damage
        print('%s deals %s damage to %s' % (self.name, damage, enemy.name))
        return enemy.health <= 0


class Demon(Enemy):
    def __init__(self, name, strength, magic, vitality):
        super().__init__(name, strength, magic, vitality)


p = Player('name', 10, 10, 10, 'gender', 'race')
e1 = Demon('Shade', 5, 5, 10)


Commands = {'quit': Player.quit, 'help': Player.help, 'stab': Player.stab, 'fireball': Player.fireball,
            'heal': Player.heal, 'status': Player.status, 'rest': Player.rest, 'escape': Player.escape,
            'encounter': Player.encounter}

p.name = input('Select character name: ')
print("Type 'help' to get a list of commands")


while p.health > 0:
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                Commands[c](p)
                commandFound = True
                break
        if not commandFound:
            print("Command not found")


