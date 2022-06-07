from requests import session
from sqlalchemy.orm import Session

from . import models,schemas

def create_tree(db: Session,trees,tree_name):
    new_tree=models.Tree(tree=trees,name=tree_name)
    db.add(new_tree)
    db.commit()
    db.refresh(new_tree)
    return new_tree.id

def create_node(db:Session, node_val,tree_ids):
    new_node=models.Node(value=node_val,tree_id=tree_ids)
    db.add(new_node)
    db.commit()
    db.refresh(new_node)
    return new_node.id

    
