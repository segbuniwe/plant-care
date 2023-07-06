from fastapi import APIRouter, Depends
from queries.plants import (
    PlantOut,
    PlantsOut,
    PlantsRepo,
)
from typing import List

router = APIRouter()


@router.get("/api/plants", response_model=List[PlantsOut])
def list_recipes(repo: PlantsRepo = Depends()):
    return repo.list_plants()


@router.get("/api/plants/{plant_id}", response_model=PlantOut)
def list_one_recipe(plant_id: int, repo: PlantsRepo = Depends()):
    return repo.get_plant_by_id(plant_id)
