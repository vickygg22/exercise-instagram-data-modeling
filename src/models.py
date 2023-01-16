import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(40))
    password = Column(String(40))
    first_name = Column(String(30))
    last_name = Column(String(40))
    email = Column(String(50))
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_type = Column(String(30))
    post_details = Column(String(300))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to = relationship(User)

class Reel(Base):
    __tablename__ = 'reel'
    id = Column(Integer, primary_key=True)
    reel_details = Column(String(300))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    users_reel = relationship(User)

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to = relationship(User)
    user_from_id = Column(Integer, ForeignKey('follower.id'))
    user_from = relationship(Follower)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    reel_id = Column(Integer, ForeignKey('reel.id'))
    reel = relationship(Reel)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(String(300))
    date = Column(DateTime)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to = relationship(User)
    user_from_id = Column(Integer, ForeignKey('follower.id'))
    user_from = relationship(Follower)
    reel_id = Column(Integer, ForeignKey('reel.id'))
    reel = relationship(Reel)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
