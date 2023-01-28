from sqlalchemy import Column, Integer, String, DateTime, true
from datetime import date, datetime
from pydantic import BaseModel
from db import Base
from typing import Optional


class UserTable(Base):
    __tablename__ = "login_info"
    id = Column(Integer, primary_key=true)
    userid = Column(String)
    usernm = Column(String)
    password = Column(String)
    email = Column(String)
    main_grade = Column(String)
    sub_grade = Column(String)
    empno = Column(String)
    hp = Column(String)
    status = Column(String)
    createid = Column(String)
    updateid = Column(String)


# createdate = Column(DateTime)
# updatedate = Column(DateTime)


class User(BaseModel):
    id: int
    userid: str
    usernm: str
    password: str
    email: str
    main_grade: str
    sub_grade: str
    empno: str
    hp: str
    status: str
    createid: str
    updateid: str


# createdate : DateTime
# updatedate : DateTime
class User_(User):
    id: int


class Users(BaseModel):
    userid: str


class IDPASSWORD(BaseModel):
    userid: str
    password: str


class UserInfo(BaseModel):
    id: int
    userid: str
    usernm: str
    email: str
    main_grade: str
    sub_grade: str
    empno: str
    hp: str
    status: str
    createid: str
    updateid: str


class ModelMapTable(Base):
    __tablename__ = "model_map"
    model_group = Column(String, primary_key=true)
    model_name = Column(String, primary_key=true)
    seq = Column(Integer, primary_key=true)
    x = Column(String)
    y = Column(String)
    z = Column(String)
    createdate = Column(DateTime)
    createid = Column(String)
    updatedate = Column(DateTime)
    updateid = Column(String)


class ModelMap(BaseModel):
    model_group: str
    model_name: str
    seq: int
    x: str
    y: str
    z: str
    createdate: date
    createid: str
    updatedate: date
    updateid: str
    id: Optional[int]


class DeleteModelMap(BaseModel):
    model_group: str
    model_name: str
    seq: int


class MachineTable(Base):
    __tablename__ = "machine_info"
    main_group = Column(String)
    code = Column(String, primary_key=true)
    codename = Column(String)
    manageno = Column(String)
    status = Column(String)
    createdate = Column(DateTime)
    createid = Column(String)
    updatedate = Column(DateTime)
    updateid = Column(String)


class MachineMap(BaseModel):
    main_group: str
    code: str
    codename: str
    manageno: str
    status: str
    createdate: date
    createid: str
    updatedate: date
    updateid: str


class PeripheralsTable(Base):
    __tablename__ = "peripherals_info"
    code = Column(String, primary_key=true)
    codename = Column(String)
    manageno = Column(String)
    x = Column(String)
    y = Column(String)
    z = Column(String)
    status = Column(String)
    createdate = Column(DateTime)
    createid = Column(String)
    updatedate = Column(DateTime)
    updateid = Column(String)


class PeripheralsMap(BaseModel):
    code: str
    codename: str
    manageno: str
    x: str
    y: str
    z: str
    status: str
    createdate: date
    createid: str
    updatedate: date
    updateid: str


class MachineRepairHistoryTable(Base):
    __tablename__ = "machine_repair_history"
    company = Column(String, primary_key=true)
    factory = Column(String, primary_key=true)
    repairno = Column(String, primary_key=true)
    model_group = Column(String, primary_key=true)
    repairdate = Column(DateTime)
    repairtime = Column(Integer)
    repaircomp = Column(String)
    repairissue = Column(String)
    sparepart = Column(String)
    repairstory = Column(String)
    repairamt = Column(Integer)
    repairuserid = Column(String)
    repairusernm = Column(String)
    remark = Column(String)
    createdate = Column(DateTime)
    createid = Column(String)
    updatedate = Column(DateTime)
    updateid = Column(String)


class MachineRepairHistoryMap(BaseModel):
    company: str
    factory: str
    repairno: str
    model_group: str
    repairdate: date
    repairtime: int
    repaircomp: str
    repairissue: str
    sparepart: str
    repairstory: str
    repairamt: int
    repairuserid: str
    repairusernm: str
    remark: str
    createdate: date
    createid: str
    updatedate: date
    updateid: str
