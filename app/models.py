
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime, JSON
from .database import Base
import datetime

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }


class Result(Base, DictMixIn):

    __tablename__ = "Results"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True)
    job_enqueued_at = Column(DateTime)
    job_started_at = Column(DateTime)
    input = Column(String)
    result = Column(JSON)