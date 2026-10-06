from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session
from security.audit import log_access

router = APIRouter()

class VisitIn(BaseModel):
    patient_id: int
    doctor_id: int
    visit_date: datetime
    complaint: str | None = None
    diagnosis_code: str | None = None
    notes: str | None = None

@router.post("/")
def create_visit(data: VisitIn, user_id: int = 0, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO visits (patient_id, doctor_id, visit_date, complaint, diagnosis_code, notes)
        VALUES (:patient_id, :doctor_id, :visit_date, :complaint, :diagnosis_code, :notes)
        RETURNING id
    """), data.dict()).fetchone()
    log_access(db, user_id, "visits", row[0], "create")
    db.commit()
    return {"id": row[0]}

@router.get("/{visit_id}")
def get_visit(visit_id: int, user_id: int = 0, db: Session = Depends(get_session)):
    v = db.execute(text("SELECT * FROM visits WHERE id=:i"), {"i": visit_id}).fetchone()
    if not v: raise HTTPException(404)
    log_access(db, user_id, "visits", visit_id, "read")
    db.commit()
    return dict(v._mapping)
