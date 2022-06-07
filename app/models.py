from sqlalchemy import Column, ForeignKey,Integer,String,PickleType
from sqlalchemy.orm import relationship
from .database import Base

class Tree(Base):
    __tablename__="trees"

    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    name=Column(String(100))
    tree=Column(PickleType)

    node_relationship = relationship("Node",back_populates="main_tree")

class Node(Base):
    __tablename__="nodees"

    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    value=Column(Integer)
    tree_id=Column(Integer,ForeignKey("trees.id"))

    main_tree=relationship("Tree",back_populates="node_relationship")