from RocketSeat.NLW.src.models.settings.connection import db_connection_handler
from RocketSeat.NLW.src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError, NoResultFound

class CheckInRepository:
    def insert_check_in(self, attendee_id: str) -> str:
            with db_connection_handler.cursor() as database:
                try:
                    check_in = (
                        CheckIns(attendeId=attendee_id)
                    )
                    database.session.add(check_in)
                    database.session.commit()
                    return attendee_id
                except IntegrityError:
                    raise Exception('Checkin já cadastrado!')
                except Exception as exception:
                    database.session.rollback()
                    raise exception
