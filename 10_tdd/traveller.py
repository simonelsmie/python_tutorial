class Traveller:
    def __init__(self, name, type, origin, destination):
        self.name = name
        self.type = type
        self.origin = origin
        self.destination = destination
        self.packed = False
        self.passport = False
        self.suitcase = []