from pydantic import BaseModel
from queries.client import Queries
import requests
from keys import PERENUAL_API_KEY


class PlantsIn(BaseModel):
    common_name: str


class PlantsOut(PlantsIn):
    id: int
    default_image: dict


class PlantOut(PlantsIn):
    id: int
    default_image: dict
    watering: str
    soil: list
    growth_rate: str
    # maintenance: str
    # medicinal: str
    # poisonous_to_humans: str
    # poisonous_to_pets: str
    indoor: bool
    care_level: str


class PlantsRepo(Queries):
    COLLECTION = "plants"

    def list_plants(self):
        url = "https://perenual.com/api/species-list"
        params = {"key": PERENUAL_API_KEY, "page": 1}
        res = requests.get(url, params=params)
        plants = res.json()
        print(plants)
        return plants["data"]

    def get_plant_by_id(self, plant_id: int):
        url = f"https://perenual.com/api/species/details/{plant_id}"
        params = {
            "key": PERENUAL_API_KEY,
        }
        res = requests.get(url, params=params)
        data = res.json()
        return data
