# import json
from app.db.db import initialize_db

db = initialize_db()


def read_wrestler():
    # with open("data/wrestlers.json") as stream:
    # wrestlers = json.load(stream)
    table = db.Table("wrestlers")
    response = table.scan()
    wrestlers = response.get("Items", [])

    return wrestlers


def get_wrestler(position: int):
    # with open("data/wrestlers.json") as stream:
    #     wrestlers = json.load(stream)

    # return position
    table = db.Table("wrestlers")
    response = table.scan()
    wrestlers = response.get("Items", [])

    for wrestler in wrestlers:
        if wrestler["id"] == position:
            return wrestler


def search_wrestler(query):
    # with open("data/wrestlers.json") as stream:
    #     wrestlers = json.load(stream)
    table = db.Table("wrestlers")
    response = table.scan()
    wrestlers = response.get("Items", [])

    output_dict = [x for x in wrestlers if query.lower() in x["name"].lower()]

    return output_dict
