def users_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "role": user["role"],
        "hashed_password": user["hashed_password"]
    }

def userlist_serial(users) -> list:
    return[users_serial(user) for user in users]

def individual_serial(presence) -> dict:
    return {
        "id": str(presence["_id"]),
        "prof": presence["prof"],
        "student": presence["student"],
        "presence": presence["presence"]
    }

def list_serial(presences) -> list:
    return[individual_serial(presence) for presence in presences]