from db.base import Base
from db.models.assignment_type import AssignmentType
from db.models.person import Person
from db.models.person_assignment import PersonAssignment
from db.models.usage_log import UsageLog
from db.engine import engine
def init_db():
    Base.metadata.create_all(bind=engine)