from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/")
def list_doctors(spec: str | None = None, db: Session = Depends(get_session)):
    sql = """
        SELECT d.id, u.full_name, d.spec, d.cabinet
        FROM doctors d JOIN users u ON u.id = d.user_id
        WHERE d.active
    """
    params = {}
    if spec:
        sql += " AND d.spec = :s"
        params['s'] = spec
    return [dict(r._mapping) for r in db.execute(text(sql), params).fetchall()]

@router.get("/{doctor_id}/load")
def load(doctor_id: int, db: Session = Depends(get_session)):
    row = db.execute(text("""
        SELECT COUNT(*) FILTER (WHERE visit_date >= NOW() - INTERVAL '7 days') AS week,
               COUNT(*) FILTER (WHERE visit_date >= NOW() - INTERVAL '30 days') AS month
        FROM visits WHERE doctor_id = :d
    """), {"d": doctor_id}).fetchone()
    return {"week": row[0], "month": row[1]}
