from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[str]
    latitude: Optional[str]
    phone: Optional[str]
    website_url: Optional[str]
    state: str
    street: Optional[str]

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.brewery_type}) - "
            f"{self.city}, {self.state_province}, {self.country}, "
            f"{self.website_url or 'brak strony'}"
        )


def pobierz_browary(limit: int = 20) -> list[Brewery]:
    response = requests.get(
        "https://api.openbrewerydb.org/v1/breweries",
        params={"per_page": limit},
        timeout=10,
    )
    response.raise_for_status()
    dane = response.json()
    return [Brewery(**{k: v for k, v in b.items() if k in Brewery.__dataclass_fields__}) for b in dane]


if __name__ == "__main__":
    browary = pobierz_browary(20)
    for browar in browary:
        print(browar)