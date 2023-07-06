from fastapi import APIRouter, Depends
from queries.favorites import (
    FavoritesRepo,
    FavoritesIn,
    FavoritesOut,
    Favorites,
)
from authenticator import authenticator


router = APIRouter()


@router.post("/api/favorites", response_model=FavoritesOut)
def create_favorite(
    favorite: FavoritesIn,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: FavoritesRepo = Depends(),
):
    account_id = account_data["id"]
    return repo.create(account_id, favorite.dict())


@router.get("/api/favorites/mine", response_model=Favorites)
def list_favorites_for_current_account(
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: FavoritesRepo = Depends(),
):
    account_id = account_data["id"]
    return {"favorites": repo.get_all_for_account(account_id)}


@router.delete("/api/favorites/{favorite_id}")
def delete_favorite(
    favorite_id: str,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: FavoritesRepo = Depends(),
):
    return repo.delete(favorite_id=favorite_id, account_id=account_data["id"])


@router.put("/api/favorites/{favorite_id}", response_model=FavoritesOut)
def update_favorite(
    favorite: FavoritesIn,
    favorite_id: str,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: FavoritesRepo = Depends(),
):
    return repo.update(
        favorite_id=favorite_id,
        favorite=favorite.dict(),
        account_id=account_data["id"],
    )
