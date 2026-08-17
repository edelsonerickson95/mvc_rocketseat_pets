from src.models.sqlite.entities.pets import PetsTable
from .pet_list_controller import PetListController


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Pikachu", type="Eletrico", id=5),
            PetsTable(name="Charmander", type="fogo", id=9),
        ]


def test_list_pets():
    controller = PetListController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Pikachu", "id": 5},
                {"name": "Charmander", "id": 9},
            ],
        }
    }

    assert response == expected_response
