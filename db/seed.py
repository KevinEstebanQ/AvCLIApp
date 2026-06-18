from db.engine import SessionLocal
from db.models.assignment_type import AssignmentType
from db.models.person import Person

def seed_assignment_types():
    types = ["mics", "audio", "video", "plataforma"]
    with SessionLocal() as session:
        for t in types:
            exists = session.query(AssignmentType).filter_by(name=t).first()
            if not exists:
                session.add(AssignmentType(name=t))
        session.commit()
