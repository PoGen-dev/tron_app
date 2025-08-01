from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import database, models, schemas, tron_service

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Tron Wallet Info Service")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/wallet-info", response_model=schemas.WalletInfo)
def wallet_info(payload: schemas.WalletRequest, db: Session = Depends(get_db)):
    address = payload.address.strip()

    try:
        info = tron_service.get_wallet_info(address)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Tron error: {exc}")

    db.add(models.RequestLog(wallet_address=address))
    db.commit()
    return info


@app.get("/requests", response_model=schemas.PaginatedLogs)
def read_requests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    total = db.query(models.RequestLog).count()
    items = (
        db.query(models.RequestLog)
        .order_by(models.RequestLog.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return {"total": total, "items": items}
