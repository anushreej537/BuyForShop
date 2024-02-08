from datetime import datetime,timedelta
import os
from fastapi import APIRouter,UploadFile,File,Depends
from .models import *
from .pydantic_models import UserData,Categoryitem,Subcategoryitem,Categoryid,Deletecategory,Deletesubcategory,Subcategoryid,Branddetail,Updatebranddetail,Deletebranddetail
app = APIRouter()

@app.post('/reg')
async def register_data(data:UserData):
    if await Register.exists(email=data.email):
        return {'email already exist'}
    else:
        obj = await Register.create(name=data.name, 
                                    email=data.email,
                              password=data.password)
        return {'obj':obj, 'message':'register successfully'}
        
@app.post("/category/")
async def create_category(data:Categoryitem = Depends(),
                          category_image:UploadFile=File(...)):
    if await Category.exists(name=data.name):
        return {"status":False, "message":"Category altready Exists"}

    else:
        FILEPATH = "static/images/category/"

        if not os.path.isdir(FILEPATH):
            os.mkdir(FILEPATH)

        filename = category_image.filename
        extension = filename.split(".")[1]
        imagename = filename.split(".")[0]

        if extension not in ["png","jpg","jpeg"]:
            return {"status":"error", "detial":"File extension not allowed"}
        
        dt = datetime.now()
        dt_timestamp = round(datetime.timestamp(dt))

        modified_image_name = imagename+"_"+str(dt_timestamp)+"_"+extension
        genrated_name =  FILEPATH+modified_image_name
        file_contant = await category_image.read()

        with open(genrated_name, "wb")as file:
            file.write(file_contant)
            file.close()

        category_obj = await Category.create(category_image=genrated_name,
                                             name=data.name,
                                             description=data.description)
        return {'category_obj':category_obj}    

@app.get('/category_all_data')
async def all_data_of_category():
    obj = await Category.all()
    return {'obj':obj}

@app.delete('/delcategory/')
async def del_category(data:Deletecategory):
    await Category.get(id=data.id).delete()
    return {'message':'category delete successfully'}

@app.put('/category_update/')
async def category_update(data:Categoryid = Depends(),
                          category_image:UploadFile=File(...)):
    getid = await Category.get(id=data.id)

    FILEPATH = "static/images/category/"

    if not os.path.isdir(FILEPATH):
        os.mkdir(FILEPATH)

    filename = category_image.filename
    extension = filename.split(".")[1]
    imagename = filename.split(".")[0]

    if extension not in ["png","jpg","jpeg"]:
        return {"status":"error", "detial":"File extension not allowed"}
        
    dt = datetime.now()
    dt_timestamp = round(datetime.timestamp(dt))

    modified_image_name = imagename+"_"+str(dt_timestamp)+"_"+extension
    genrated_name =  FILEPATH+modified_image_name
    file_contant = await category_image.read()

    with open(genrated_name, "wb")as file:
        file.write(file_contant)
        file.close()

    await Category.filter(id=data.id).update(name=data.name,description=data.description,
                                           category_image=genrated_name)
    return {'category update successful'}

@app.get('/subcategory_all_data')
async def all_data_of_subcategory():
    obj = await Subcategory.all()
    return {'obj':obj}

@app.post('/subcategory/')
async def create_subcategory(data:Subcategoryitem = Depends(),
                          subcategory_image:UploadFile=File(...)):
    if await Category.exists(id=data.category_id):
        category_obj = await Category.get(id = data.category_id)
        
        if await Subcategory.exists(name=data.name):
            return {'status':False, 'message':'name already exist'}

        else:
            FILEPATH = "static/images/subcategory/"

            if not os.path.isdir(FILEPATH):
                os.mkdir(FILEPATH)

            filename = subcategory_image.filename
            extension = filename.split(".")[1]
            imagename = filename.split(".")[0]

            if extension not in ["png","jpg","jpeg"]:
                return {"status":"error", "detial":"File extension not allowed"}
            
            dt = datetime.now()
            dt_timestamp = round(datetime.timestamp(dt))

            modified_image_name = imagename+"_"+str(dt_timestamp)+"_"+extension
            genrated_name =  FILEPATH+modified_image_name
            file_contant = await subcategory_image.read()

            with open(genrated_name, "wb")as file:
                file.write(file_contant)
                file.close()

            subcategory_obj = await Subcategory.create(subcategory_image=genrated_name,
                                                name=data.name,
                                                category=category_obj,
                                                description=data.description)
            return {'subcategory_obj':subcategory_obj}    

@app.put('/subcategory_update/')
async def subcategory_update(data:Subcategoryid = Depends(),
                          subcategory_image:UploadFile=File(...)):
    getid = await Subcategory.get(id=data.id)

    FILEPATH = "static/images/category/"

    if not os.path.isdir(FILEPATH):
        os.mkdir(FILEPATH)

    filename = subcategory_image.filename
    extension = filename.split(".")[1]
    imagename = filename.split(".")[0]

    if extension not in ["png","jpg","jpeg"]:
        return {"status":"error", "detial":"File extension not allowed"}
        
    dt = datetime.now()
    dt_timestamp = round(datetime.timestamp(dt))

    modified_image_name = imagename+"_"+str(dt_timestamp)+"_"+extension
    genrated_name =  FILEPATH+modified_image_name
    file_contant = await subcategory_image.read()

    with open(genrated_name, "wb")as file:
        file.write(file_contant)
        file.close()

    await Subcategory.filter(id=data.id).update(name=data.name,description=data.description,
                                           subcategory_image=genrated_name)
    return {'subcategory update successful'}

@app.delete('/delsubcategory/')
async def del_subcategory(data:Deletesubcategory):
    await Subcategory.get(id=data.id).delete()
    return {'message':'subcategory delete successfully'}


@app.post('/brand_detail/')
async def brand_data(data:Branddetail):
    obj = await Brand.create(brand_name=data.brand_name)
    return {'obj':obj}

@app.get('/get_brand_detail')
async def get_brand_data():
    obj = await Brand.all()
    return {'obj':obj}

@app.put('/update_brand_detail/')
async def update_brand_data(data:Updatebranddetail):
    await Brand.filter(id=data.id).update(brand_name = data.brand_name)
    return {'brand detail updated successfully'}

@app.delete('/delete_brand_detail')
async def delete_brand_data(data:Deletebranddetail):
    await Brand.get(id=data.id).delete()
    return {'message':'delete brand detail successfully'}