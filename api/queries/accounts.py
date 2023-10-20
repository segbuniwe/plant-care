from pydantic import BaseModel
from queries.client import Queries


class DuplicateAccountError(ValueError):
    pass


class AccountIn(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str


class AccountOut(BaseModel):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str


class AccountOutWithHashedPassword(AccountOut):
    hashed_password: str


class AccountRepo(Queries):
    COLLECTION = "accounts"

    def get_account_by_username(self, username: str):
        account = self.collection.find_one({"username": username})
        if account is None:
            return None
        account["id"] = str(account["_id"])
        return AccountOutWithHashedPassword(**account)

    def get_account_by_email(self, email: str) -> AccountOutWithHashedPassword:
        account = self.collection.find_one({"email": email})
        if account is None:
            return None
        account["id"] = str(account["_id"])
        return AccountOutWithHashedPassword(**account)

    def create(self, info: AccountIn, hashed_password: str) -> AccountOut:
        account = info.dict()
        if (
            self.get_account(account["email"]) is not None
            or self.get_account(account["username"]) is not None
        ):
            raise DuplicateAccountError
        account["hashed_password"] = hashed_password
        del account["password"]
        response = self.collection.insert_one(account)
        account["id"] = str(response.inserted_id)
        return AccountOutWithHashedPassword(**account)
