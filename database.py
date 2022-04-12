from sqlalchemy import create_engine, Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("mysql+pymysql://root:Ponchick123@127.0.0.1:3306/DBASE")


class User1(Base):
    __tablename__ = 'user1'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    tel_num = Column(String(15), nullable=False)
    mail = Column(String(25), nullable=False)

    def __repr__(self):
        return f"<USER1> {self.id} {self.name}"


class User2(Base):
    __tablename__ = 'user2'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    program = Column(String(60), nullable=False)
    num = Column(Integer, primary_key=True)
    date_start = Column(DateTime())
    date_end = Column(DateTime())
    status = Column(String(20), nullable=False)


Base.metadata.create_all(engine)

# USER ADD
Session = sessionmaker(bind=engine)
session = Session()


