from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from loguru import logger

'''when declared out side of the SessionManager class, the 'engine' 
will continue to exist even when an instance of the SessionManager
is disposed'''

engine = create_engine(
    "mysql+pymysql://demo:Demo123!@192.168.124.70/demo", echo=True)
Base = automap_base()
Base.prepare(autoload_with=engine)


def get_db():
    try:
        db = SessionManager()
        yield db
    except Exception as e:
        logger.debug(str(e))
    finally:
        db.close()


class SessionManager:

    def __init__(self):
        # engine = create_engine(
        #     "mysql+pymysql://demo:Demo123!@192.168.124.70/demo", echo=True)
        # Base = automap_base()
        # Base.prepare(autoload_with=engine)

        self.m = Base.classes.m
        self.d = Base.classes.d

        self.session = Session(engine)

    def close(self):
        self.session.close()
