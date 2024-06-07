from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase,mapped_column, Mapped
from typing import List, Optional




Base = DeclarativeBase()
engine = create_engine("sqlite://", echo=True)

class Base(DeclarativeBase):
     pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]





if __name__ == "__main__":
    Base.metadata.create_all(engine)

     