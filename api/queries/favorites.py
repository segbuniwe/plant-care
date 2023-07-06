from pydantic import BaseModel
from queries.client import Queries
from typing import List
from bson.objectid import ObjectId


class FavoritesIn(BaseModel):
    plant_name: str
    image: str


class FavoritesOut(FavoritesIn):
    id: str
    account_id: str


class Favorites(BaseModel):
    favorites: List[FavoritesOut]


class FavoritesRepo(Queries):
    COLLECTION = "favorites"

    def create(self, account_id: str, favorite: FavoritesIn):
        favorite["account_id"] = account_id
        self.collection.insert_one(favorite)
        favorite["id"] = str(favorite["_id"])
        return FavoritesOut(**favorite)

    def get_all_for_account(self, account_id: str):
        results = []
        for favorite in self.collection.find({"account_id": account_id}):
            favorite["id"] = str(favorite["_id"])
            results.append(favorite)
        return results

    def delete(self, favorite_id: str, account_id: str):
        result = self.collection.delete_one(
            {"_id": ObjectId(favorite_id), "account_id": account_id}
        )
        return result.deleted_count > 0

    def update(self, favorite_id: str, favorite: FavoritesIn, account_id: str):
        updated_favorite = favorite
        self.collection.update_one(
            {"_id": ObjectId(favorite_id), "account_id": account_id},
            {"$set": updated_favorite},
        )
        updated_favorite["id"] = favorite_id
        updated_favorite["account_id"] = account_id
        return FavoritesOut(**updated_favorite)
