class Character:
    def __init__(self, char_object):
        self.name = char_object["name"]
        self.status = char_object["status"]
        self.species = char_object["species"]
        self.location = char_object["location"]["name"]
        self.last_episode = char_object["episode"][-1]