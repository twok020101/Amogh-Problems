from tokenize import Name
from pydantic import NoneStr
from . import crud

class Node(object):
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

    def new_tree(self,db,name):
        return crud.create_tree(db,self,name)
    

    def insert(self,db,data,tree_id) ->None:
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                    crud.update_tree(db,self,tree_id)
                    return crud.create_node(db,data,tree_id)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                    crud.update_tree(db,self,tree_id)
                    return crud.create_node(db,data,tree_id)
                else:
                    self.right.insert(data)
        else:
            self.data=data
            return crud.create_node(db,self,tree_id)

    def delete(self,data,tree_id,db):
        if self.data:
            if self.data==data:
                del self.data
                crud.update_tree(db,self,tree_id)
                return {"message":"Node deleted successfully"}
            elif self.data<data and self.left!=None:
                self.delete(self.left,data)
            elif self.data>data and self.right!=None:
                self.delete(self.right,data)
            else:
                return {"message":"Node not found"}

    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res

    def preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)
            return res
    
        
    

            
    