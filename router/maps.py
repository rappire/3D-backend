import sys

sys.path.append("..")
from fastapi import APIRouter, Depends
from db import SessionLocal
from sqlalchemy.orm import Session
from models import ModelMap, ModelMapTable, ModelMap_, DeleteModelMap, Users
from typing import List
from datetime import datetime

router = APIRouter(prefix="/map", tags=["maps"])


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/{model_group}", response_model=List[ModelMap_])
async def getUsers(model_group: str, db: Session = Depends(get_db)):
    try:
        model_data = (
            db.query(ModelMapTable)
            .filter(ModelMapTable.model_group == model_group)
            .all()
        )
        data = []
        for i in range(len(model_data)):
            data.insert(
                i,
                ModelMap_(
                    id=i,
                    model_group=model_data[i].model_group,
                    model_name=model_data[i].model_name,
                    seq=model_data[i].seq,
                    x=model_data[i].x,
                    y=model_data[i].y,
                    z=model_data[i].z,
                    createdate=model_data[i].createdate,
                    createid=model_data[i].createid,
                    updatedate=model_data[i].updatedate,
                    updateid=model_data[i].updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"


@router.get("", response_model=List[ModelMap_])
async def getUsers(db: Session = Depends(get_db)):
    try:
        model_data = (
            db.query(ModelMapTable).filter(ModelMapTable.model_group != "").all()
        )

        data = []
        for i in range(len(model_data)):
            data.insert(
                i,
                ModelMap_(
                    id=i,
                    model_group=model_data[i].model_group,
                    model_name=model_data[i].model_name,
                    seq=model_data[i].seq,
                    x=model_data[i].x,
                    y=model_data[i].y,
                    z=model_data[i].z,
                    createdate=model_data[i].createdate,
                    createid=model_data[i].createid,
                    updatedate=model_data[i].updatedate,
                    updateid=model_data[i].updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"


@router.put("update/{modellist}")  # 데이터 수정
async def update_map(item: ModelMap, db: Session = Depends(get_db)):
    try:
        List = (
            db.query(ModelMapTable)
            .filter(ModelMapTable.model_group == item.model_group)
            .filter(ModelMapTable.model_name == item.model_name)
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
        List = f"insert into model_map (model_group,model_name,seq,x,y,z,createdate,createid,updatedate,updateid) values ('{item.model_group}','{item.model_name}','{item.seq}',{item.x},{item.y},{item.z},now(),'{item.createid}',now(),'{item.updateid}')"
        db.execute(List)
        db.commit()
        return f"{item.model_group},{item.model_name} added..."
    except Exception:
        return "ERROR"


@router.delete("updelete/")  # 데이터 삭제
async def add_map(item: DeleteModelMap, db: Session = Depends(get_db)):
    try:
        List = (
            db.query(ModelMapTable)
            .filter(ModelMapTable.model_group == item.model_group)
            .filter(ModelMapTable.model_name == item.model_name)
            .filter(ModelMapTable.seq == item.seq)
            .first()
        )
        if List is None:
            return "None"
        db.delete(List)
        db.commit()
        return f"{List.model_name} deleted..."
    except Exception:
        return "ERROR"
