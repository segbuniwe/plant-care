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
        username: str,
        accounts: AccountRepo,
    ):
        # Use your repo to get the account based on the
        # username (which could be an email)
        return accounts.get_account(username)

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
        return account.email, AccountOut(**account.dict())


authenticator = PlantCareAuthenticator(os.environ["SIGNING_KEY"])