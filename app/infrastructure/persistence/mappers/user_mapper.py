from app.domain.users.entity import Users, UserId, UserEmail, UserHashedPassword


async def user_from_dict_to_entity(data: dict) -> Users:
    return Users(
        id=UserId(data["id"]),
        email=UserEmail(data["email"]),
        hashed_password=UserHashedPassword(data["hashed_password"]),
    )
