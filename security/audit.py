from sqlalchemy import text

def log_access(db, user_id: int, entity: str, entity_id: int, action: str):
    """Пишет запись в журнал аудита."""
    db.execute(text("""
        INSERT INTO audit_log (user_id, action, entity, entity_id)
        VALUES (:u, :a, :e, :i)
    """), {"u": user_id, "a": action, "e": entity, "i": entity_id})
