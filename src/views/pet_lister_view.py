from src.controllers.pet_list_controller import PetListControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class PetListerView(ViewInterface):
    def __init__(self, controller: PetListControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()
        return HttpResponse(satus_code=200, body=body_response)
