import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship


class ViewedPlayers(SqlAlchemyBase):
    __tablename__ = 'viewed_players'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=True)
    steam_id = sqlalchemy.Column(sqlalchemy.String(20), nullable=True)

    user = relationship("User", back_populates="viewed_players")