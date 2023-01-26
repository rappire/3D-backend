import sys

sys.path.append("..")
from fastapi import APIRouter, Depends
from db import SessionLocal
from sqlalchemy.orm import Session
from models import MachineRepairHistoryTable, MachineRepairHistoryMap
from typing import List
from datetime import datetime

router = APIRouter(prefix="/machinerepairhistory", tags=["machinerepairhistory"])


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("", response_model=List[MachineRepairHistoryMap])
async def machinerepairhistory(db: Session = Depends(get_db)):
    try:
        MachineRepairHistory_data = (
            db.query(MachineRepairHistoryTable)
            .filter(MachineRepairHistoryTable.repairno != "")
            .all()
        )
        data = []
        for i in range(len(MachineRepairHistory_data)):
            data.insert(
                i,
                MachineRepairHistoryMap(
                    company=MachineRepairHistory_data[i].company,
                    factory=MachineRepairHistory_data[i].factory,
                    repairno=MachineRepairHistory_data[i].repairno,
                    model_group=MachineRepairHistory_data[i].model_group,
                    repairdate=MachineRepairHistory_data[i].repairdate,
                    repairtime=MachineRepairHistory_data[i].repairtime,
                    repaircomp=MachineRepairHistory_data[i].repaircomp,
                    repairissue=MachineRepairHistory_data[i].repairissue,
                    sparepart=MachineRepairHistory_data[i].sparepart,
                    repairstory=MachineRepairHistory_data[i].repairstory,
                    repairamt=MachineRepairHistory_data[i].repairamt,
                    repairuserid=MachineRepairHistory_data[i].repairuserid,
                    repairusernm=MachineRepairHistory_data[i].repairusernm,
                    remark=MachineRepairHistory_data[i].remark,
                    createdate=MachineRepairHistory_data[i].createdate,
                    createid=MachineRepairHistory_data[i].createid,
                    updatedate=MachineRepairHistory_data[i].updatedate,
                    updateid=MachineRepairHistory_data[i].updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"


@router.put("update/{MachineRepair}")  # 데이터 수정
async def update_map(item: MachineRepairHistoryMap, db: Session = Depends(get_db)):
    try:
        List = (
            db.query(MachineRepairHistoryTable)
            .filter(MachineRepairHistoryTable.company == item.company)
            .filter(MachineRepairHistoryTable.factory == item.factory)
            .filter(MachineRepairHistoryTable.repairno == item.repairno)
            .filter(MachineRepairHistoryTable.model_group == item.model_group)
            .first()
        )
        if List is None:
            return "None"
        List.repairdate = item.repairdate
        List.repairtime = item.repairtime
        List.repaircomp = item.repaircomp
        List.repairissue = item.repairissue
        List.sparepart = item.sparepart
        List.repairstory = item.repairstory
        List.repairamt = item.repairamt
        List.repairuserid = item.repairuserid
        List.repairusernm = item.repairusernm
        List.remark = item.remark
        List.updateid = item.updateid
        List.updatedate = datetime.now()
        db.add(List)
        db.commit()
        return f"{item.repairno} updated..."
    except Exception:
        return "ERROR"


@router.post("add/{mrepairlist}")  # 데이터 인서트
async def add_map(item: MachineRepairHistoryMap, db: Session = Depends(get_db)):
    try:
        MachineRepairHistory_data = (
            db.query(MachineRepairHistoryTable)
            .filter(MachineRepairHistoryTable.repairno != "")
            .all()
        )
        repairno = "mr" + str(len(MachineRepairHistory_data) + 1)
        List = f"insert into machine_repair_history (company,factory,repairno,model_group,repairdate,repairtime,repaircomp,repairissue,sparepart,repairstory,repairamt,repairuserid,repairusernm,remark,createid,createdate,updateid,updatedate) values ('{item.company}','{item.factory}','{repairno}','{item.model_group}',now(),'{item.repairtime}','{item.repaircomp}','{item.repairissue}','{item.sparepart}','{item.repairstory}','{item.repairamt}','{item.repairuserid}','{item.repairusernm}','{item.remark}','{item.createid}',now(),'{item.updateid}',now())"
        db.execute(List)
        db.commit()

        return f"{item.repairno} added..."
    except Exception:
        return "ERROR"


@router.delete("delete/{mrepairlist}")  # 데이터 삭제
async def add_map(mrepairlist: str, db: Session = Depends(get_db)):
    try:
        List = (
            db.query(MachineRepairHistoryTable)
            .filter(MachineRepairHistoryTable.repairno == mrepairlist)
            .first()
        )
        if List is None:
            return "None"
        db.delete(List)
        db.commit()
        return f"{List.repairno} deleted..."
    except Exception:
        return "ERROR"
