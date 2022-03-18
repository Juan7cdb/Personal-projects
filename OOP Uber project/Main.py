from lib2to3.pgen2.driver import Driver
from Car import Car
from Account import Account

if __name__ =="__main__":
    
    car = Car("AMD 154", Account("Andres Herrera", "1121916785"))
    print(vars(car))
    print(vars(car.driver))
    
    
    # car = Car()
    # car.license = "AMH 123"
    # car.driver = "Andres Herrera"
    
    # print(vars(car))
    
    # car2 = Car()
    # car2.license = "SGT 256"
    # car2.driver = "Federico Gutierrez"
    
    # print(vars(car2))
    
    # user = Account()
    # user.id = 123456
    # user.name = "Juan Felipe Robayo"
    # user.document = 1121916807
    # user.email = "juandavid@pharmed.com"
    # user.password = "nolevoyadecir10+"
    

    