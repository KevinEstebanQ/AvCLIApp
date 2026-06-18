from db.base import Base
from sqlalchemy import Column, Integer, String
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class PersonAssignment(Base):
    __tablename__ = 'person_assignments'
    
    person_id: Mapped[int] = mapped_column(ForeignKey('people.id'), primary_key=True)
    assignment_type_id: Mapped[int] = mapped_column(ForeignKey('assignment_types.id'), primary_key=True)

    # relationships
    person: Mapped["Person"] = relationship(back_populates="assignments")
    assignment_type: Mapped["AssignmentType"] = relationship(back_populates="person_assignments")