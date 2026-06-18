import csv
from db.engine import SessionLocal
from db.models.assignment_type import AssignmentType
from db.models.person import Person, PersonRole
from db.models.person_assignment import PersonAssignment
from db.models.usage_log import UsageLog
from pathlib import Path

def import_from_csv(filepath: Path):
    with SessionLocal() as session:
        with open(filepath, newline="", encoding="UTF-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"].strip()
                role_str = row["role"].strip().lower()
                assignments = [ass.strip().lower() for ass in row["assignments"].split("|") if ass.strip()]
                
                try:
                    role = PersonRole(role_str)
                except ValueError:
                    print(f"unknow role: {role_str}, for person: {name} - defaulting to none")
                    role = PersonRole.NONE

                person = session.query(Person).filter_by(name=name).first()
                if person:
                    print(f"[UPDATING] {name}")
                    person.role = role
                else: 
                    print(f"[INSERT] {name}")
                    person = Person(name=name, role=role)
                    session.add(person)

                session.flush()
                session.refresh(person)
                for assignment_name in assignments:

                    # get or create the assignment type
                    assignment_type = session.query(AssignmentType).filter_by(name=assignment_name).first()
                    if not assignment_type:
                        print(f"  [NEW ASSIGNMENT TYPE] {assignment_name}")
                        assignment_type = AssignmentType(name=assignment_name)
                        session.add(assignment_type)
                        session.flush()

                    existing = session.query(PersonAssignment).filter_by(
                        person_id=person.id,
                        assignment_type_id=assignment_type.id
                    ).first()

                    if not existing:
                        session.add(PersonAssignment(person_id=person.id,
                                                      assignment_type_id=assignment_type.id))
                session.commit()
            print("Done importing")





