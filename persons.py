# persons.py

from datetime import datetime
from flask import abort
from flask import make_response


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


PERSONS = {
    "Adam": {
        "fname": "Adam",
        "lname": "Smith",
        "personID": "111222333",
        "timestamp": get_timestamp(),
    },
    "John": {
        "fname": "John",
        "lname": "Adams",
        "personID": "222333444",
        "timestamp": get_timestamp(),
    },
    "Ben": {
        "fname": "Ben",
        "lname": "Johnson",
        "personID": "333444555",
        "timestamp": get_timestamp(),
    }
}


def createPerson(person):
    person.get("lname",)
    lname = person.get("lname")
    fname = person.get("fname", "")
    personID = person.get("personID", "")

    if fname and lname and personID not in PERSONS:
        PERSONS[lname] = {
            "lname": lname,
            "fname": fname,
            "personID": personID,
            "timestamp": get_timestamp(),
            
        }
        return PERSONS[lname], 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )


def get_all_persons():
    return list(PERSONS.values())


def get_person_by_id(personID):
    if personID in PERSONS:
        return PERSONS[personID]
    else:
        abort(
            404, f"Person with ID {personID} not found"
        )


def update_person_by_id(lname, person, personID):
    if personID in PERSONS:
        PERSONS[personID]["fname"] = person.get("fname", PERSONS[personID]["fname"])
        PERSONS[personID]["lname"] = person.get("lname", PERSONS[personID]["lname"])
        PERSONS[personID]["personID"] = person.get("personID", PERSONS[personID]["personID"])
        PERSONS[personID]["timestamp"] = get_timestamp()
        return PERSONS[personID]
    else:
        abort(
            404,
            f"Person with ID {personID} not found"
        )


def delete_person_by_id(personID):
    print(personID)
    if personID in PERSONS:
        del PERSONS[personID]
        return make_response(
            f"{personID} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with ID {personID} not found"
        )
