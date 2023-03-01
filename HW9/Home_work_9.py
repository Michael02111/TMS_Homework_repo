import random

class GameCharacter:
    __status = 'Active'

    def __init__(self, name, health,
                 level):
        self.name = name
        self.health = health
        self.level = level


    def speak(self):
        print('Hi, my name is ' + self.name + ' I\'m feeling good')


    def string (self):
        print('I\'m ready for battle')

    def get_status(self):
        print(self.name, ' Status: ', self.__status)


    def change_status(self):
        self.__status = 'Deactivated'
        print('That was hardcore mode, you account has been deactivated!')



class Villain(GameCharacter):

    def __init__(self,name, health,
                 level):
        GameCharacter.__init__(self, name, health,
                               level)

    def speak(self):
        print('Hi, my name is ' + self.name + ' and I will kill you')


    def kill(self):
        self.health = 0
        print('Bang-bang, now you\'re dead')
        a = random.randint(1, 5)
        if a == 5:
            self.change_status()
            print('Death number: ', a)
        else:
            print('Lucky number ', a)



Michael = GameCharacter('Michael', 100, 1)
Veron = Villain('Veron', 100, 2)




Michael.speak()
Veron.speak()
Michael.string()
print(Michael.health)
Veron.kill()
print(Michael.health)
Michael.get_status()
Veron.get_status()





