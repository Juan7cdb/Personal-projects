from Car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []
    
    def __init__(self, license, driver, typeCarAccepted, seatMaterial):
        super.__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatMaterial