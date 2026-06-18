from db.base import Base
from typing import Optional
from datetime import date
from sqlalchemy import Text, Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class UsageLog(Base):
    __tablename__ = 'usage_log'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('people.id'), nullable=False)
    assignment_type_id: Mapped[Optional[int]] = mapped_column(ForeignKey('assignment_types.id'), nullable=True)
    used_on: Mapped[date] = mapped_column(Date, nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    person: Mapped["Person"] = relationship(back_populates="usage_logs")
    assignment_type: Mapped[Optional["AssignmentType"]] = relationship(back_populates="usage_logs")