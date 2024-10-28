from importer import Importer
from register import Register

class Core:
    def __init__(self):
        pass
    
    def call(self):
        rounds = self.__to_import()
        self.__to_register(rounds)
    
    def __to_import(self):
        importer = Importer()
        return importer.get_rounds()
    
    def __to_register(self, data):
        register = Register()
        register.save_data(data)

core_instance = Core()
core_instance.call()
