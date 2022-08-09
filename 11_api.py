import requests
from character import Character

url = "https://rickandmortyapi.com/api"

# response = requests.get(f"{url}/character")
# # print(response.json()["results"])
# results = response.json()["results"]
# list_of_characters = []
# for character in results:
#     list_of_characters.append(
#         {
#             "name": character["name"],
#             "status": character["status"]
#         }
#     )
# print(list_of_characters)

def get_characters():
    response = requests.get(f"{url}/character")
    results = response.json()["results"]
    list_of_characters = []
    for character in results:
        list_of_characters.append(
            {
                "name": character["name"],
                "status": character["status"]
            }
        )
    return list_of_characters

characters = get_characters()

def show_only_alive(list_of_characters):
    results = []
    for character in list_of_characters:
        if character["status"] == "Alive":
            results.append(character["name"])
    return results


print(show_only_alive(characters))


def get_rick():
    response = requests.get(f"{url}/character")
    results = response.json()["results"]
    for character in results:
        if character["name"] == "Rick Sanchez":
            return character


rick_dict = get_rick()
# print(rick_dict)

rick = Character(rick_dict)
print(rick.name, rick.last_episode, rick.status, rick.species, rick.location)


# GET - return basic information - query params
# POST - create in api/db - body
# DELETE - deleting
# PUT - updating in api/db


# requests.post()
# requests.delete()
# requests.put()