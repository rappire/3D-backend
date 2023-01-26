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
        for i in range(len(Peripherals_data)):
            data.insert(
                i,
                PeripheralsMap(
                    code=Peripherals_data[i].code,
                    codename=Peripherals_data[i].codename,
                    manageno=Peripherals_data[i].manageno,
                    x=Peripherals_data[i].x,
                    y=Peripherals_data[i].y,
                    z=Peripherals_data[i].z,
                    status=Peripherals_data[i].status,
                    createdate=Peripherals_data[i].createdate,
                    createid=Peripherals_data[i].createid,
                    updatedate=Peripherals_data[i].updatedate,
                    updateid=Peripherals_data[i].updateid,
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
        for i in range(len(Peripherals_data)):
            data.insert(
                i,
                PeripheralsMap(
                    code=Peripherals_data[i].code,
                    codename=Peripherals_data[i].codename,
                    manageno=Peripherals_data[i].manageno,
                    x=Peripherals_data[i].x,
                    y=Peripherals_data[i].y,
                    z=Peripherals_data[i].z,
                    status=Peripherals_data[i].status,
                    createdate=Peripherals_data[i].createdate,
                    createid=Peripherals_data[i].createid,
                    updatedate=Peripherals_data[i].updatedate,
                    updateid=Peripherals_data[i].updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"
