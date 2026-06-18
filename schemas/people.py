from pydantic import BaseModel
from datetime import date

class DbPerson(BaseModel):
    id: int
    name: str
    last_used: date | None = None
    role: str