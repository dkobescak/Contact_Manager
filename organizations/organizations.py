
class Organization:
    def __init__(self, name, oib, address):
        self.name = name
        self.oib = oib
        self.address = address
        self.employees = []
        self.customers = []
