from sqlmodel import  SQLModel, Session
from sqlalchemy import create_engine

host = 'localhost'
db_name = 'lotteca'
user = 'andreurbanski'
pwd = '1234'
port =  '5432'

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)
    print ("DB Engine started")


def get_session():
    with Session(engine) as session:
        yield session