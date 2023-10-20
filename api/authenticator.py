import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.accounts import (
    AccountRepo,
    AccountOut,
    AccountOutWithHashedPassword,
)


class PlantCareAuthenticator(Authenticator):
    async def get_account_data(
        self,
        identifier: str,
        accounts: AccountRepo,
    ):
        is_email = "@" in identifier
        account = (
            accounts.get_account_by_email(identifier)
            if is_email
            else accounts.get_account_by_username(identifier)
        )

        return account

    def get_account_getter(
        self,
        accounts: AccountRepo = Depends(),
    ):
        # Return the accounts. That's it.
        return accounts

    def get_hashed_password(self, account: AccountOutWithHashedPassword):
        # Return the encrypted password value from your
        # account object
        return account.hashed_password

    def get_account_data_for_cookie(self, account: AccountOut):
        # Return the username and the data for the cookie.
        # You must return TWO values from this method.
        return account.username, AccountOut(**account.dict())


authenticator = PlantCareAuthenticator(os.environ["SIGNING_KEY"])
