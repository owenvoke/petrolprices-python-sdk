import requests_mock

from petrolprices import PetrolPrices

petrolprices = PetrolPrices("abcdefghijklmnopqrstuvwxyz123457890")


def test_search_with_no_results():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://app.petrolprices.com/geojson/2/0/0/0/price/5?lat=1.2345678901&longitude=1.2345678901",
            json={
                "error": False,
                "limitExceed": False,
                "data": {"type": "FeatureCollection", "features": []},
                "search_id": 1,
                "message": "Petrol Station Fuel List Listed by Coordinates",
            },
        )
        results = petrolprices.search(1.2345678901, 1.2345678901)

        assert type(results) == dict
        assert results.get("data") == []
