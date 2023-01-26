import sys

sys.path.append("..")
from fastapi import APIRouter, Depends
from db import SessionLocal
from sqlalchemy.orm import Session
from models import MachineMap, MachineTable
from typing import List

router = APIRouter(prefix="/machine", tags=["machine"])


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("", response_model=List[MachineMap])
async def getMachines(db: Session = Depends(get_db)):
    try:
        Machine_data = db.query(MachineTable).filter(MachineTable.code != "").all()

        data = []
        for i in range(len(Machine_data)):
            data.insert(
                i,
                MachineMap(
                    id=i,
                    main_group=Machine_data[i].main_group,
                    code=Machine_data[i].code,
                    codename=Machine_data[i].codename,
                    manageno=Machine_data[i].manageno,
                    status=Machine_data[i].status,
                    createdate=Machine_data[i].createdate,
                    createid=Machine_data[i].createid,
                    updatedate=Machine_data[i].updatedate,
                    updateid=Machine_data[i].updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"


@router.post("/{code}", response_model=List[MachineMap])
async def getMachine(code: str, db: Session = Depends(get_db)):
    try:
        Machine_data = db.query(MachineTable).filter(MachineTable.code == code).all()
        data = []
        for i in range(len(Machine_data)):
            data.insert(
                i,
                MachineMap(
                    id=i,
                    main_group=Machine_data[i].main_group,
                    code=Machine_data[i].code,
                    codename=Machine_data[i].codename,
                    manageno=Machine_data[i].manageno,
                    status=Machine_data[i].status,
                    createdate=Machine_data[i].createdate,
                    createid=Machine_data[i].createid,
                    updatedate=Machine_data[i].updatedate,
                    updateid=Machine_data[i].updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"
