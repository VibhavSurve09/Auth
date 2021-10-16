from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Users(Base):
    __tablename__="Users"
    userid=Column(Integer, primary_key=True,index=True)
    username=Column(String())
    email=Column(String)
    password=Column(String)
    address=Column(String)