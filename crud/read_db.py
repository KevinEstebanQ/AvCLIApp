from db.engine import SessionLocal
from db.models.assignment_type import AssignmentType
from db.models.person import Person
from db.models.person_assignment import PersonAssignment
from db.models.usage_log import UsageLog
from sqlalchemy import Select
from typing import List
from schemas.people import DbPerson

def show_per_role(role: str = "none",) -> List[DbPerson] | None:
    if role not in ["none", "anciano", "siervo"]:
        raise ValueError
    stmt = Select(Person).where(Person.role == role)
    with SessionLocal() as session:
        result = session.execute(statement=stmt).scalars().all()
        if result:
            return [DbPerson(id=p.id, name=p.name, last_used=p.last_used, role=p.role) for p in result]
        else:
            return None