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

class Product_detail(BaseModel):
    category_id:int
    subcategory_id:int
    brand_id:int
    product_name:str
    product_price:int
    product_code:int
    description:str
    offer_price:int

class Deleteproductdetail(BaseModel):
    id:int