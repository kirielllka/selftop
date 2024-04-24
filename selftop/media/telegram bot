import abc
import copy
class Pasta(abc.ABC):
    def __init__(self,type:str)->None:
        self.type = None
        self.souse = None
        self.add = None
        self.ins = None

    @abc.abstractmethod
    def cooking_pasta(self):
        pass

    def set_type(self):
        self.type = input('Select type:')
    def souse_pasta(self):
        self.souse = input(f'Select the souse for {self.type}:')


    def addect(self):
        self.add = input(f'Select adectives for {self.type}:')


    def inst(self):
        self.ins = input(f'Select instance for {self.type}:')

class Pasta_cook(Pasta):
    def __init__(self):
        super().__init__(type)

    def cooking_pasta(self):
            self.set_type()
            print('\nGood\n')
            self.souse_pasta()
            print('\nnice chose\n')
            self.addect()
            print('\n looks delicious\n')
            self.inst()
            print(f'\n you create good reciepe for {self.type}')
            print(f'{self.type},{self.add},{self.souse},{self.ins}')


class Game():
    def __init__(self):
        self.components = []

    def add_components(self, *args):
        for i in(args):
            self.components.append(i)



    def __str__(self):
        return ','.join(self.components)

class Game_builder(abc.ABC):



    @abc.abstractmethod
    def add_interface(self):
        pass

    @abc.abstractmethod
    def add_history(self):
        pass

    @abc.abstractmethod
    def add_mechanic(self):
        pass

    @abc.abstractmethod
    def get_game(self):
        pass


class IndiBuilder(Game_builder):
        def __init__(self):
            self.game = Game()

        def add_interface(self):
            self.game.add_components('simple indi interface')

        def add_history(self):
            self.game.add_components('interesting history about Benni')

        def add_mechanic(self):
            self.game.add_components('Weapon', 'Digging', 'Cars')

        def get_game(self):
            return self.game


class Director:
    def __init__(self, builder):
        self.builder = builder

    def make_game(self):

        self.builder.add_interface()
        self.builder.add_history()
        self.builder.add_mechanic()

    def get_game(self):
        return self.builder.get_game()


class Adress():
    def __init__(self, street,city, country):
        self.street = street
        self.city = city
        self.country = country
    def __str__(self):
        return f'{self.street},{self.city},{self.country}'
class Person():
    def __init__(self, name:str,address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} live at {self.address}'

if __name__ == '__main__':
    # Indi1 = IndiBuilder()
    # director1 = Director(Indi1)
    # director1.make_game()
    # game = director1.get_game()
    # print()

    John = Person('john',Adress('12 wall street','NY',"USA"))
    Jane = copy.deepcopy(John)
    Jane.address.street = '13 Wall street'
    Jane.name = 'jane'
    print(Jane)
    print(John)




