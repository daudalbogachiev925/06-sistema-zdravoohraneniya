from fastapi import FastAPI
from routes import patients, doctors, visits, prescriptions, lab

app = FastAPI(title="МИС API")

app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(doctors.router, prefix="/doctors", tags=["doctors"])
app.include_router(visits.router, prefix="/visits", tags=["visits"])
app.include_router(prescriptions.router, prefix="/prescriptions", tags=["prescriptions"])
app.include_router(lab.router, prefix="/lab", tags=["lab"])

@app.get("/health")
def health(): return {"status": "ok"}
