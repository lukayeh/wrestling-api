import json

from app.db.db import initialize_db

db = initialize_db()


def read_wrestler():
    table = db.Table("wrestlers")
    response = table.scan()
    wrestlers = response.get("Items", [])

    return json.dumps(wrestlers, indent=1, sort_keys=True)


def query_wrestler(query):
    queriesList = []
    for x in query:
        if x[1] is not None:
            queriesList.append(x)

    table = db.Table("wrestlers")
    response = table.scan()
    wrestlers = response.get("Items", [])

    if len(queriesList) == 0:
        return read_wrestler()

    if len(queriesList) > 1:
        return json.dumps(
            {
                "message": "query list can only be 1 currently..",
                "category": "failed",
                "status": 400,
            }
        )

    queryKey = queriesList[0][0]
    queryValue = query = queriesList[0][1]

    wrestlers = [x for x in wrestlers if queryValue.lower() in x[queryKey].lower()]

    return json.dumps(wrestlers, indent=1, sort_keys=True)


def create_wrestler(wrestler):

    table = db.Table("wrestlers")
    name = wrestler.name
    billFrom = wrestler.billFrom
    signatureMoves = wrestler.signatureMoves
    finishingMoves = wrestler.finishingMoves
    dob = wrestler.dob
    works_for = wrestler.works_for
    birthName = wrestler.birthName
    nickNames = wrestler.nickNames

    try:
        table.put_item(
            Item={
                "name": name,
                "billFrom": billFrom,
                "signatureMoves": signatureMoves,
                "finishingMoves": finishingMoves,
                "dob": dob,
                "works_for": works_for,
                "birthName": birthName,
                "nickNames": nickNames,
            }
        )
    except Exception as x:
        return {
            "message": f"Faled to create: {name} with error {x}",
            "category": "failed",
            "status": 400,
        }

    return {
        "message": f"Successfully created: {name}",
        "category": "success",
        "status": 200,
    }
