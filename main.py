from itertools import tee
from typing import final
from fastapi import Depends, FastAPI
from requests import Session
from app import models,schemas,crud,trees
from app.trees import Node
from app.database import SessionLocal,engine

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.post("/trees")
def trees(val:schemas.TreeNew,db: Session=Depends(get_db)):
    tree=Node(val.val,val.Name)
    return tree

app.post("/trees/{tree_id}/nodes")
def nodes(tree_id:int,val:schemas.NodeNew,db: Session=Depends(get_db)):
    tree=crud.get_tree(db,tree_id)
    return trees.insert(tree,db,val.node_val,tree_id)

app.delete("/trees/{tree_id}/nodes/{node_id}")
def delete(tree_id,node_id,db: Session=Depends(get_db)):
    val=crud.get_node_val(db,node_id,tree_id)
    tree=crud.get_tree(db,tree_id)
    return trees.delete(tree,val,tree_id,db)

app.post("/trees/{tree_id}/inorder")
def inorder(tree_id,db: Session=Depends(get_db)):
    tree=crud.get_tree(db,tree_id)
    return trees.inorder(tree)

app.post("/trees/{tree_id}/preorder")
def preorder(tree_id,db: Session=Depends(get_db)):
    tree=crud.get_tree(db,tree_id)
    return trees.preorder(tree)

app.post("/trees/{tree_id}/postorder")
def postorder(tree_id,db: Session=Depends(get_db)):
    tree=crud.get_tree(db,tree_id)
    return trees.postorder(tree)