from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/item/{item_id}")     # Path parameters
def path_param(item_id):
    return {"data" : item_id}


@app.get("/product/{pro_id}")
def path_param(pro_id :int):       # Path parameter with data type, it uses pydantic under the hood to provide this functionality (str, float, bool)
    return {"data" : pro_id}


# Here path operation order matters

@app.get("/user/me")
def profile():
    return {'data' : 'Current : Ashish Chaudhary'}


@app.get("/user/{user_id}")
def profile(user_id :str):
    return {'data' : f'Current : {user_id}'}

'''
Because path operations are evaluated in order, 
you need to make sure that the path for /users/me is declared before the one for /users/{user_id}

'''
'''
Otherwise, the path for /users/{user_id} would match also for /users/me, "thinking" that it's receiving a parameter user_id with a value of "me"
'''


### Predefined values
### If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.

from enum import Enum

class Cars(str, Enum):  # By inheriting from str the API docs will be able to know that the values must be of type string and will be able to render correctly.
    bmw = 'BMW'
    maybach = 'Maybach'
    audi = 'Audi'
    pagani = 'Pagani'


@app.get('/getcar/{car_name}')
def car(car_name :Cars):
    if car_name is Cars.bmw:            # Compare enumeration members
        return {"Model" : "Gmtr990", "message" : "Welcome to the Luxury"}
    
    if car_name.value == "Audi":        # Get the enumeration value
        return {"Model" : "Q7", "message" : "Excellent Choice"}
    
    return {"model_name" : car_name, "message" : "Not Available"}       # Return enumeration members



#Path parameters containing paths¶
'''
Let's say you have a path operation with a path /files/{file_path}.

But you need file_path itself to contain a path, like home/johndoe/myfile.txt.

So, the URL for that file would be something like: /files/home/johndoe/myfile.txt.

OpenAPI support¶
OpenAPI doesn't support a way to declare a path parameter to contain a path inside, as that could lead to scenarios that are difficult to test and define.

Nevertheless, you can still do it in FastAPI, using one of the internal tools from Starlette.

And the docs would still work, although not adding any documentation telling that the parameter should contain a path.

Path convertor¶
Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:


/files/{file_path:path}
In this case, the name of the parameter is file_path, and the last part, :path, tells it that the parameter should match any path.
'''

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}