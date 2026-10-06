from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class LabIn(BaseModel):
    patient_id: int
    test_name: str
    result: str
    unit: str | None = None
    normal_range: str | None = None

@router.post("/")
def create(data: LabIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO lab_results (patient_id, test_name, result, unit, normal_range)
        VALUES (:patient_id, :test_name, :result, :unit, :normal_range)
        RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/patient/{patient_id}")
def by_patient(patient_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT * FROM lab_results WHERE patient_id=:p ORDER BY taken_at DESC
    """), {"p": patient_id}).fetchall()]
