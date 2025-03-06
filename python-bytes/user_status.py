class UserStatus:
    def __init__(self, user_id: int, message: str) -> None:
        self.user_id = user_id
        self.message = message

    def __bytes__(self) -> bytes:
        return b"".join(
            [
                self.user_id.to_bytes(4, "little", signed=False),
                self.message.encode("utf-8"),
            ]
        )


if __name__ == "__main__":
    user_status = UserStatus(42, "Away from keyboard \N{PALM TREE}")
    print(bytes(user_status))
