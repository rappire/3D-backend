import sys

sys.path.append("..")
from fastapi import APIRouter, Depends
from models import User, UserTable, User_, IDPASSWORD, UserInfo
from db import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt
from typing import List
import sha256

router = APIRouter(prefix="", tags=["users"])


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


JWT_SECRET = "1q2w3e4r!@#"
JWT_ALGORITHM = "HS256"
AES_KEY = "#%!#asdf7263!&#*"


@router.post("/userstoken/{userid}")
async def getUsers(userid: str, db: Session = Depends(get_db)):
    try:
        token = []
        User_data = db.query(UserTable).filter(UserTable.userid == userid).all()
        access_token = create_access_token(
            data={
                "ID": User_data[0].userid,
                "main_grade": User_data[0].main_grade,
                "sub_grade": User_data[0].sub_grade,
            },
        )
        token.append(access_token)
        token.append(User_data[0].userid)
        token.append(User_data[0].usernm)
        return token
    except Exception:
        return "ERROR"


# Make token
def create_access_token(data: dict = None, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": datetime.utcnow() + timedelta(hours=expires_delta)})
    else:
        to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=15)})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    payload = jwt.decode(encoded_jwt, JWT_SECRET, algorithms=JWT_ALGORITHM)

    return encoded_jwt


@router.post("/logincheck")
async def checkUser(item: IDPASSWORD, db: Session = Depends(get_db)):
    try:
        User_data = db.query(UserTable).filter(UserTable.userid == item.userid).all()
        if len(User_data) == 0:
            return False  # "등록되지 않은 아이디입니다."
        key = sha256.encrypt_sha(item.password)
        if key != User_data[0].password:
            return False  # "비밀번호가 일치하지 않습니다."
        else:
            return True  # "로그인 성공"
    except Exception:
        return "ERROR"


@router.post("/userstokencheck/{token_key}")
async def getUsers(token_key: str):
    try:
        payload = jwt.decode(token_key, JWT_SECRET, algorithms=JWT_ALGORITHM)
        access_token = create_access_token(
            data={
                "ID": payload["ID"],
                "main_grade": payload["main_grade"],
                "sub_grade": payload["sub_grade"],
            },
        )
        return access_token
    except KeyError:
        return "N"  # False
    except jwt.ExpiredSignatureError:
        return "N"  # False
    except Exception:
        return "ERROR"


@router.post("/users/{userid}", response_model=List[User_])
async def getUsers(userid: str, db: Session = Depends(get_db)):
    try:
        User_data = db.query(UserTable).filter(UserTable.userid == userid).all()
        data = []
        if len(User_data) == 0:
            return data
        for i in range(len(User_data)):
            # data.insert(i,User_(id =i,userid=User_data[i].userid,usernm=User_data[i].usernm,password=User_data[i].password,email="test",main_grade="123",sub_grade="645",empno="45",hp="464",status="156",createdate="datetime.now()",createid="1436",updatedate="datetime.now()",updateid="36"))
            data.insert(
                i,
                User_(
                    id=i,
                    userid=User_data[i].userid,
                    usernm=User_data[i].usernm,
                    password=User_data[i].password,
                    email=User_data[i].email,
                    main_grade=User_data[i].main_grade,
                    sub_grade=User_data[i].sub_grade,
                    empno=User_data[i].empno,
                    hp=User_data[i].hp,
                    status=User_data[i].status,
                    createid=User_data[i].createid,
                    updateid=User_data[i].updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"


@router.get("/users", response_model=List[User_])
async def getUsers(db: Session = Depends(get_db)):
    try:
        User_data = db.query(UserTable).filter(UserTable.userid != "").all()
        data = []
        if len(User_data) == 0:
            return data
        # data.insert(i,User_(id =i,userid=User_data[i].userid,usernm=User_data[i].usernm,password=User_data[i].password,email="test",main_grade="123",sub_grade="645",empno="45",hp="464",status="156",createdate="datetime.now()",createid="1436",updatedate="datetime.now()",updateid="36"))
        for i in range(len(User_data)):
            data.insert(
                i,
                User_(
                    id=i,
                    userid=User_data[i].userid,
                    usernm=User_data[i].usernm,
                    password=User_data[i].password,
                    email=User_data[i].email,
                    main_grade=User_data[i].main_grade,
                    sub_grade=User_data[i].sub_grade,
                    empno=User_data[i].empno,
                    hp=User_data[i].hp,
                    status=User_data[i].status,
                    createid=User_data[i].createid,
                    updateid=User_data[i].updateid,
                ),
            )
        return data
    except Exception:
        return "ERROR"


@router.put("/useruppass")  # 비밀번호 데이터 수정
async def update_users(item: IDPASSWORD, db: Session = Depends(get_db)):
    try:
        user = db.query(UserTable).filter(UserTable.userid == item.userid).first()
        if user is None:
            return "None"
        user.password = sha256.encrypt_sha(item.password)
        user.updateid = item.userid
        db.add(user)
        db.commit()
        return item
    except Exception:
        return "ERROR"


@router.put("/userupinfo")  # 데이터 수정
async def update_users(item: UserInfo, db: Session = Depends(get_db)):
    try:
        user = db.query(UserTable).filter(UserTable.userid == item.userid).first()
        if user is None:
            return "None"
        user.usernm = item.usernm
        user.email = item.email
        user.main_grade = item.main_grade
        user.sub_grade = item.sub_grade
        user.empno = item.empno
        user.hp = item.hp
        user.status = item.status
        user.updateid = item.userid
        db.add(user)
        db.commit()
        return item
    except Exception:
        return "ERROR"


@router.post("/usersadd/{userid}")  # 데이터 인서트
async def add_users(item: User, db: Session = Depends(get_db)):
    try:
        check = db.query(UserTable).filter(UserTable.userid == item.userid).first()
        if check is not None:
            return f"'{check.userid}' already exists"

        enpassword = sha256.encrypt_sha(item.password)
        user = f"insert into login_info (userid,usernm,password,email,main_grade,sub_grade,empno,hp,status,createid,updateid) values ('{item.userid}','{item.usernm}','{enpassword}','{item.email}','{item.main_grade}','{item.sub_grade}','{item.empno}','{item.hp}','{item.status}','{item.createid}','{item.updateid}')"
        db.execute(user)
        db.commit()
        return "{item.userid} inserted..."
    except Exception:
        return "ERROR"


@router.delete("/usersdelete/{userid}")  # 데이터 삭제
async def update_users(userid: str, db: Session = Depends(get_db)):
    try:
        user = db.query(UserTable).filter(UserTable.userid == userid).first()
        if user is None:
            return "None"
        db.delete(user)
        db.commit()
        return f"{userid} deleted..."
    except Exception:
        return "ERROR"
