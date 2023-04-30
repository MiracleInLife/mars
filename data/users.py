import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from .viewed_players import ViewedPlayers
from .viewed_matchs import ViewedMatchs
from sqlalchemy.orm import relationship


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String(20), nullable=True, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    viewed_players = relationship("ViewedPlayers", back_populates="user")
    viewed_matchs = relationship("ViewedMatchs", back_populates="user")