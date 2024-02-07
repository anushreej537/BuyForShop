from pydantic import BaseModel


class UserData(BaseModel):
    name:str
    email:str
    password:str
    
class Categoryitem(BaseModel):
    name:str
    description:str

class Categoryid(BaseModel):
    id:int

class Deletecategory(BaseModel):
    id:int 
    
class Subcategoryitem(BaseModel):
    category_id:int
    name:str
    description:str