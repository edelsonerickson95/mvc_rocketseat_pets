from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.pet_list_controller import PetListController
from src.views.pet_lister_view import PetListerView


def pet_lister_compose():
    model = PetsRepository(db_connection_handler)
    controller = PetListController(model)
    view = PetListerView(controller)

    return view
