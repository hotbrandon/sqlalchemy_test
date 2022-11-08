from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db, SessionManager
from models import ModelM

router = APIRouter()


@router.get("/")
async def index(db: SessionManager = Depends(get_db)):
    '''
    adding filter is not necessary here, because sqlalchemy
    automatically join the tables based on the foreign key relationship
    '''
    rp = db.session.query(db.m)\
        .join(db.d).all()  # .filter(db.m.id == db.d.m_id)

    return {"data": dir(rp)}


@router.post("/")
async def create_md(m: ModelM, db: SessionManager = Depends(get_db)):
    ''' save data in m and d tables simultaneously'''
    master = db.m(name="amy")
    master.d_collection.append(db.d(d_name="son1"))
    master.d_collection.append(db.d(d_name="son2"))

    db.session.add(master)

    db.session.commit()

    return {"status": True}
