class Traveller:
    def __init__(self, name, type, origin, destination):
        self.name = name
        self.type = type
        self.origin = origin
        self.destination = destination
        self.packed = False
        self.passport = False
        self.suitcase = []
        self.flights = 0

    def do_packing(self, list_of_items):
        for item in list_of_items:
            self.suitcase.append(item)
        self.packed = True

    def get_passport(self):
        if self.packed == True:
            self.passport = True

    def grouped(self):
        self.type = "Group"

    def lets_fly(self):
        self.flights += 1