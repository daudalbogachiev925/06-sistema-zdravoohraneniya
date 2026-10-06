from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class PatientIn(BaseModel):
    full_name: str
    birth: date
    gender: str
    policy: str
    phone: str | None = None
    address: str | None = None

@router.get("/")
def list_patients(q: str | None = None, db: Session = Depends(get_session)):
    sql = "SELECT * FROM patients"
    params = {}
    if q:
        sql += " WHERE full_name ILIKE :q OR policy ILIKE :q"
        params['q'] = f"%{q}%"
    return [dict(r._mapping) for r in db.execute(text(sql), params).fetchall()]

@router.post("/")
def create_patient(data: PatientIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO patients (full_name, birth, gender, policy, phone, address)
        VALUES (:full_name, :birth, :gender, :policy, :phone, :address)
        RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_session)):
    p = db.execute(text("SELECT * FROM patients WHERE id=:i"), {"i": patient_id}).fetchone()
    if not p: raise HTTPException(404)
    return dict(p._mapping)

@router.get("/{patient_id}/history")
def history(patient_id: int, db: Session = Depends(get_session)):
    sql = open('sql/patient_history.sql').read() if False else """
        SELECT v.id, v.visit_date, v.complaint, v.diagnosis_code
        FROM visits v WHERE v.patient_id = :p ORDER BY v.visit_date DESC
    """
    return [dict(r._mapping) for r in db.execute(text(sql), {"p": patient_id}).fetchall()]
