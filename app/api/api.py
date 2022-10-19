import json


def read_wrestler():
    with open("data/wrestlers.json") as stream:
        wrestlers = json.load(stream)

    return wrestlers


def get_wrestler(position: int):
    with open("data/wrestlers.json") as stream:
        wrestlers = json.load(stream)

        # return position

    for wrestler in wrestlers:
        if wrestler["id"] == position:
            return wrestler


def search_wrestler(query):
    with open("data/wrestlers.json") as stream:
        wrestlers = json.load(stream)

    output_dict = [x for x in wrestlers if query.lower() in x["name"].lower()]

    return output_dict
