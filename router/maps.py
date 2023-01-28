import sys

sys.path.append("..")
from fastapi import APIRouter, Depends
from db import SessionLocal
from sqlalchemy.orm import Session
from models import ModelMap, ModelMapTable, DeleteModelMap
from typing import List
from datetime import datetime

router = APIRouter(prefix="/map", tags=["maps"])


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/{model_group}", response_model=List[ModelMap])
async def getUsers(model_group: str, db: Session = Depends(get_db)):
    try:
        model_data = (
            db.query(ModelMapTable)
            .filter(ModelMapTable.model_group == model_group)
            .all()
        )
        data = []
        for i, model in enumerate(model_data):
            data.append(
                ModelMap(
                    model_group=model.model_group,
                    model_name=model.model_name,
                    seq=model.seq,
                    x=model.x,
                    y=model.y,
                    z=model.z,
                    createdate=model.createdate,
                    createid=model.createid,
                    updatedate=model.updatedate,
                    updateid=model.updateid,
                    id=i,
                )
            )
        return data
    except Exception:
        return "ERROR"


@router.get("", response_model=List[ModelMap])
async def getUsers(db: Session = Depends(get_db)):
    try:
        model_data = (
            db.query(ModelMapTable).filter(ModelMapTable.model_group != "").all()
        )
        data = []
        for i, model in enumerate(model_data):
            data.append(
                ModelMap(
                    model_group=model.model_group,
                    model_name=model.model_name,
                    seq=model.seq,
                    x=model.x,
                    y=model.y,
                    z=model.z,
                    createdate=model.createdate,
                    createid=model.createid,
                    updatedate=model.updatedate,
                    updateid=model.updateid,
                    id=i,
                )
            )
        return data
    except Exception:
        return "ERROR"


@router.put("update/{modellist}")  # 데이터 수정
async def update_map(item: ModelMap, db: Session = Depends(get_db)):
    try:
        List = (
            db.query(ModelMapTable)
            .filter(
                ModelMapTable.model_group == item.model_group,
                ModelMapTable.model_name == item.model_name,
                ModelMapTable.seq == item.seq,
            )
            .first()
        )
        if List is None:
            return "None"
        List.x = item.x
        List.y = item.y
        List.z = item.z
        List.updateid = item.updateid
        List.updatedate = datetime.now()
        db.add(List)
        db.commit()
        return f"{item.model_name} updated..."
    except Exception:
        return "ERROR"


@router.post("upadd/{modellist}")  # 데이터 인서트
async def add_map(item: ModelMap, db: Session = Depends(get_db)):
    try:
        L = ModelMapTable(
            model_group=item.model_group,
            model_name=item.model_name,
            seq=item.seq,
            x=item.x,
            y=item.y,
            z=item.z,
            createdate=datetime.now(),
            updatedate=datetime.now(),
            createid=item.createid,
            updateid=item.updateid,
        )
        db.add(L)
        db.commit()
        return f"{item.model_group},{item.model_name} added..."
    except Exception:
        return "ERROR"


@router.delete("updelete/")  # 데이터 삭제
async def add_map(item: DeleteModelMap, db: Session = Depends(get_db)):
    try:
        List = (
            db.query(ModelMapTable)
            .filter(
                ModelMapTable.model_group == item.model_group,
                ModelMapTable.model_name == item.model_name,
                ModelMapTable.seq == item.seq,
            )
            .first()
        )
        if List is None:
            return "None"
        db.delete(List)
        db.commit()
        return f"{List.model_name} deleted..."
    except Exception:
        return "ERROR"
