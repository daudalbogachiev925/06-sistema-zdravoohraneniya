from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class PrescriptionIn(BaseModel):
    visit_id: int
    drug: str
    dosage: str | None = None
    duration_days: int | None = None
    notes: str | None = None

@router.post("/")
def create(data: PrescriptionIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO prescriptions (visit_id, drug, dosage, duration_days, notes)
        VALUES (:visit_id, :drug, :dosage, :duration_days, :notes)
        RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/visit/{visit_id}")
def list_by_visit(visit_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(
        text("SELECT * FROM prescriptions WHERE visit_id=:v"),
        {"v": visit_id}).fetchall()]
