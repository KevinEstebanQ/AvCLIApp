from db.base import Base
from datetime import date
from typing import List, Optional
from sqlalchemy import Column, Date, Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

class PersonRole(str, enum.Enum):
    ANCIANO = "anciano"
    SIERVO = "siervo"
    NONE = "none"

class Person(Base):
    __tablename__ = 'people'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_used: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    role: Mapped[Optional[PersonRole]] = mapped_column(Enum(PersonRole), nullable=True)


    # relationships
    assignments: Mapped[List['PersonAssignment']] = relationship(back_populates='person')
    usage_logs: Mapped[List['UsageLog']] = relationship(back_populates='person')