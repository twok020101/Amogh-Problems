from sqlalchemy import Column, ForeignKey,Integer,String
from sqlalchemy.orm import relationship
from .database import Base

class Tree(Base):
    __tablename__="trees"

    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    Name:Column(String(300))
    tree=Column(String(300))

class Node(Base):
    __tablename__="nodes"

    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    value=Column(Integer)
    tree_id=Column(Integer,ForeignKey("trees.id"))

    main_tree=relationship("Tree",back_populates="nodes")