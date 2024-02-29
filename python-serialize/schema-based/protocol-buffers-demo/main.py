from models import Language, User
from users_pb2 import Language as LanguageDAO
from users_pb2 import User as UserDAO
from users_pb2 import Users as UsersDAO


def main():
    buffer = serialize()
    users = deserialize(buffer)
    print(buffer)
    print(users)


def serialize():
    users = [User.fake() for _ in range(5)]
    users_dao = UsersDAO()
    for user in users:
        user_dao = UserDAO()
        user_dao.id = user.id
        user_dao.name = user.name
        user_dao.email = user.email
        user_dao.language = LanguageDAO.Value(user.language.name)
        user_dao.registered_at.FromDatetime(user.registered_at)
        users_dao.users.append(user_dao)
    return users_dao.SerializeToString()


def deserialize(buffer):
    users_dao = UsersDAO()
    users_dao.ParseFromString(buffer)
    return [
        User(
            id=user_dao.id,
            name=user_dao.name,
            email=user_dao.email,
            language=list(Language)[user_dao.language],
            registered_at=user_dao.registered_at.ToDatetime(),
        )
        for user_dao in users_dao.users
    ]


if __name__ == "__main__":
    main()
