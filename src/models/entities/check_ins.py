from RocketSeat.NLW.src.models.settings.base import Base #Base declarativa
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):#herança da base declarativa
    __tablename__ = "check_ins"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendeeId = Column(String, ForeignKey("attendees.id"))


    def __repr__(self):
        return f"CheckIns [attendeeId = {self.attendeeId}]"