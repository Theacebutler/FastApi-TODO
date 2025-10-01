from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///site.db", connect_args={"check_same_thread": False})
SessionLlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_tables():

    # import the tables here
    Base.metadata.create_all(bind=engine)



def get_db():
    db=SessionLlocal()
    try: 
        yield db
    finally:
        db.close()