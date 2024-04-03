import pytest
from RocketSeat.NLW.src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()
@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():
    event = {
        "uuid": "salve2",
        "title": "meu title",
        "slug": "opa2",
        "maximum_attendees": 20
    }
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

@pytest.mark.skip(reason="Usuário não existente")
def test_get_event_by_id():
    event_id = "salve277"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
    #print(response.title)