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

def get_tree(db:Session,tree_id):
    return db.query(models.Tree.tree).filter(models.Tree.id==tree_id).first()

def get_node_val(db:Session,node_id,tree_id):
    val=db.query(models.Node.value).filter(models.Node.id==node_id and models.Node.tree_id==tree_id)
    db.query(models.Node).filter(models.Node.id==node_id and models.Node.tree_id==tree_id).delete()
    db.commit()
    return val

def update_tree(db:Session,trees,tree_id):
    x=db.query(models.Tree).filter(models.Node.tree_id==tree_id).update({models.Tree.tree:trees},synchronize_session=False)
    return x

