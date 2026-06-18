from db.base import Base
from sqlalchemy import Column, Integer, String
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AssignmentType(Base):
    __tablename__ = 'assignment_types'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    #relationships
    person_assignments: Mapped[List["PersonAssignment"]] = relationship(back_populates="assignment_type")
    usage_logs: Mapped[List["UsageLog"]] = relationship(back_populates="assignment_type")