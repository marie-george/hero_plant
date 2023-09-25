import random


class Heros:

    def __init__(self, name, power_level, label):
        self.name = name
        self.power_level = Heros.check_power_level(power_level)
        self.label = Heros.check_label(label)

    @staticmethod
    def check_power_level(power_level):
        if power_level > 1 and power_level <= 10:
            return power_level
        else:
            raise Exception('уровень силы по 10 бальной шкале')

    @staticmethod
    def check_label(label):
        if label == 'Marvel' or label == 'DC':
            return label
        else:
            raise Exception('признак принадлежности к лейблу: DC или Marvel')

    def superpower(self):
        return f'Аааа, я {self.name}!'


def gladiators_arena(hero1, hero2):
    print('Fight!')
    print(hero1.superpower())
    print(hero2.superpower())
    powers_dif = hero1.power_level - hero2.power_level
    if powers_dif > 1:
        print(f'{hero1.name} wins!')
    elif powers_dif == 1 or powers_dif == -1:
        heros_list = [hero1.name, hero2.name]
        random_hero = random.choice(heros_list)
        print(random_hero)
    else:
        print(f'{hero2.name} wins!')


hero1 = Heros('IronMan', 9, 'Marvel')
hero2 = Heros('SuperMan', 10, 'DC')

gladiators_arena(hero1, hero2)


