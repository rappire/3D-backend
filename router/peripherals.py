import sys

sys.path.append("..")
from fastapi import APIRouter, Depends
from db import SessionLocal
from sqlalchemy.orm import Session
from models import PeripheralsMap, PeripheralsTable
from typing import List

router = APIRouter(prefix="/peripherals", tags=["peripherals"])


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("", response_model=List[PeripheralsMap])
async def getPeripherals(db: Session = Depends(get_db)):
    try:
        Peripherals_data = (
            db.query(PeripheralsTable).filter(PeripheralsTable.code != "").all()
        )
        data = []
        for i in Peripherals_data:
            data.append(
                PeripheralsMap(
                    code=i.code,
                    codename=i.codename,
                    manageno=i.manageno,
                    x=i.x,
                    y=i.y,
                    z=i.z,
                    status=i.status,
                    createdate=i.createdate,
                    createid=i.createid,
                    updatedate=i.updatedate,
                    updateid=i.updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"


@router.post("/{code}", response_model=List[PeripheralsMap])
async def getPeripheral(code: str, db: Session = Depends(get_db)):
    try:
        Peripherals_data = (
            db.query(PeripheralsTable).filter(PeripheralsTable.code == code).all()
        )
        data = []
        for i in Peripherals_data:
            data.append(
                PeripheralsMap(
                    code=i.code,
                    codename=i.codename,
                    manageno=i.manageno,
                    x=i.x,
                    y=i.y,
                    z=i.z,
                    status=i.status,
                    createdate=i.createdate,
                    createid=i.createid,
                    updatedate=i.updatedate,
                    updateid=i.updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"
