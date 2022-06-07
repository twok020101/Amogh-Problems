from tokenize import Name
from pydantic import NoneStr
from . import crud

class Node(object):
    def __init__(self,data,name) -> None:
        self.data=data
        self.left=None
        self.right=None
        self.name=name

    

    def insert(self,db,data) ->None:
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
                    return crud.create_node(db,self,)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
            return crud.create_node(db,self,tree_name)

    def delete(self,data):
        if self.data:
            if self.data==data:
                del self.data
                return {"message":"Node deleted successfully"}
            elif self.data<data and self.left!=None:
                self.delete(self.left,data)
            elif self.data>data and self.right!=None:
                self.delete(self.right,data)
            else:
                return {"message":"Node not found"}

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
            return res
    
        
    

            
    