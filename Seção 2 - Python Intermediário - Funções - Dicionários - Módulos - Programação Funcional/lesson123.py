import json
import os

# people = {
#     "nome": "Luiz Otávio 2",
#     "sobrenome": "Miranda",
#     "enderecos": [
#         {"rua": "R1", "numero": 32},
#         {"rua": "R2", "numero": 55},
#     ],
#     "altura": 1.8,
#     "numeros_preferidos": (2, 4, 6, 8, 10),
#     "dev": True,
#     "nada": None,
# }

# BASE_DIR = os.path.dirname(__file__)
# path = os.path.join(BASE_DIR, "lesson123.json")
# with open(path, "w", encoding="utf-8") as json_file:
#     json.dump(people, json_file, ensure_ascii=False, indent=2)

BASE_DIR = os.path.dirname(__file__)
path = os.path.join(BASE_DIR, "lesson123.json")
with open(path, "r", encoding="utf-8") as file:
    people = json.load(file)
    print(people)
