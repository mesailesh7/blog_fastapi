from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# check same thread: false is only for sqllite because sqllite only handles singular thread while as fastapi handles multiple threads
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


# We wanna take control when data gets commit and saved
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



class Base(DeclarativeBase):
    pass

# Dependency function
def get_db():
    with SessionLocal() as db:
        yield db
