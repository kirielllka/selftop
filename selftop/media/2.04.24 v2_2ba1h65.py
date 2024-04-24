import datetime
import pickle,json
class Car:
    def __init__(self,name_of_model:str=None,year_of_production:int=None,production:str=None,engine:int=None,color:str=None,price:int=None):
        self.name = name_of_model
        self.year = year_of_production
        self.production = production
        self.engine = engine
        self.color = color
        self.price = price
    def enter_data(self):
        self.name = input('Enter name of car:')
        self.year = int(input('Enter production year of car:'))
        self.production = input('Enter production of car')
        self.engine = int(input('Enter engine volume:'))
        self.color = input('Enter car color:')
        self.price = int(input('Enter car price:'))

    def get_data(self):
        print(self.name,self.year,self.production,self.engine,self.color,self.price )

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_production(self):
        return self.production

    def get_engine(self):
        return self.engine

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def dump_pickle(self,obj):
        with open("data.pickle", "wb") as file:
            pickle.dump(obj, file)
    def load_pickle(self):
        with open("data.pickle", "rb") as file:
            return pickle.load(file)

    def dump_json(self, obj):
        with open("data.json", "w") as fh:
            json.dump(obj, fh)

    def load_json(self):
        with open("data.json", "rb") as fh:
            return json.load(fh)


class Book():
    def __init__(self,name:str=None,year_relise:int=None,reliser:str=None,ganre:str=None,autor:str=None,price:int=None):
        self.name = name
        self.year = year_relise
        self.autor = autor
        self.reliser = reliser
        self.ganre = ganre
        self.price = price

    def enter_data(self):
        self.name = input('Enter name of book:')
        self.year = int(input('Enter relise year of book:'))
        self.autor = input('Enter autor of book:')
        self.reliser = int(input('Enter book reliser:'))
        self.ganre = input('Enter book ganre:')
        self.price = int(input('Enter book price:'))

    def get_data(self):
        print(self.name,self.year,self.autor,self.reliser,self.ganre,self.price )

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_autor(self):
        return self.autor

    def get_reliser(self):
        return self.reliser

    def get_ganre(self):
        return self.ganre

    def get_price(self):
        return self.price

    def dump_pickle(self,obj):
        with open("data.pickle", "wb") as file:
            pickle.dump(obj, file)
    def load_pickle(self):
        with open("data.pickle", "rb") as file:
            return pickle.load(file)

    def dump_json(self, obj):
        with open("data.json", "w") as fh:
            json.dump(obj, fh)

    def load_json(self):
        with open("data.json", "rb") as fh:
            return json.load(fh)



class Stadion():
    def __init__(self,name:str=None,date_of_open:str=None,country:str=None,city:str=None,capacity:int=None):
        self.name = name
        self.date = datetime.datetime.strptime(date_of_open, '%d-%m-&y').date()
        self.country = country
        self.city = city
        self.capacity = capacity

    def enter_data(self):
        self.name = input('Enter name of stadium:')
        self.date = int(input('Enter date of open trough -(01-01-24) :'))
        self.country = input('Enter country:')
        self.city = int(input('Enter city:'))
        self.capacity = input('Enter capacity:')

    def get_data(self):
        print(self.name,self.date,self.country,self.city,self.capacity)

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def dump_pickle(self,obj):
        with open("data.pickle", "wb") as file:
            pickle.dump(obj, file)
    def load_pickle(self):
        with open("data.pickle", "rb") as file:
            return pickle.load(file)

    def dump_json(self, obj):
        with open("data.json", "w") as fh:
            json.dump(obj, fh)

    def load_json(self):
        with open("data.json", "rb") as fh:
            return json.load(fh)
