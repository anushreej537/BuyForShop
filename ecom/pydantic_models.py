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
    name:str
    description:str

class Deletecategory(BaseModel):
    id:int 

class Subcategoryitem(BaseModel):
    category_id:int
    name:str
    description:str

class Subcategoryid(BaseModel):
    id:int
    name:str
    description:str

class Deletesubcategory(BaseModel):
    id:int

class Branddetail(BaseModel):
    brand_name:str

class Updatebranddetail(BaseModel):
    id:int
    brand_name:str

class Deletebranddetail(BaseModel):
    id:int