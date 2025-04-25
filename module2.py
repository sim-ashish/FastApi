from fastapi import FastAPI, Request
from path import Paths
from typing import Union


app = FastAPI()

# Query Parameters

database_records = [{"name" : "Ashish", "email" : "ashish@mail.com"},
                    {"name" : "Devarsh", "email" : "devarshpatel@mail.com"},
                    {"name" : "Dhruv", "email" : "dhruvpatel@mail.com"},
                    {"name" : "Yug", "email" : "yug@mail.com"},
                    {"name" : "Hitesh", "email" : "hitesh@mail.com"},
                    {"name" : "Yashu", "email" : "yashuuu@mail.com"},
                    {"name" : "Harsh", "email" : "harsh122@mail.com"},
                    {"name" : "Virat", "email" : "virat2003@mail.com"},
                    {"name" : "Sachin", "email" : "tendulkar@mail.com"},
                    {"name" : "Yuvraj", "email" : "uvsingh@mail.com"},
                    {"name" : "Akshay", "email" : "akki999@mail.com"},
                    {"name" : "Aalap", "email" : "aalap2000@mail.com"},
                    {"name" : "Dhoni", "email" : "mahendra@mail.com"}]

@app.get(Paths.home)
def home():
    return {'Message' : 'Welcome'}

@app.get('/records/')                   # http://127.0.0.1:8000/records/?skip=3&limit=6
def get_records(skip :int = 0, limit :int = 2):
    return database_records[skip : skip + limit]

# Optional Paramater, the below will run on python 3.10+

@app.get("/items/{item_id}")
def read_item(item_id: str, q: str | None = None):      # typehint -> str | None telling that it can either be str or None, This is a Python 3.10+ syntax for Union types using the | operator. It means that q can be either: a string or None

    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# Optional Paramater, the below will run on python < 3.10

@app.get("/items/{item_id}/")
def read_item(item_id: str, q: Union[str, None] = None):      # typehint -> str | None telling that it can either be str or None, This is a Python 3.10+ syntax for Union types using the | operator. It means that q can be either: a string or None

    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# We can also declare bool type query param 


@app.get("/donate/")
def read_item(answer: bool = False): # Here answer is queryparam not path parameter
    if answer:
        return {"Message" : "Congratulations You have donated"}
    return {"Message" : "Donate next time!"}

'''
http://127.0.0.1:8000/donate/?answer=1
or

http://127.0.0.1:8000/donate/?answer=True
or

http://127.0.0.1:8000/donate/?answer=true
or

http://127.0.0.1:8000/donate/?answer=on
or

http://127.0.0.1:8000/donate/?answer=yes

or any other case variation (uppercase, first letter in uppercase, etc), your function will see the parameter answer with a bool value of True. Otherwise as False.
'''

# We can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.
# And you don't have to declare them in any specific order, They will be detected by name.


'''
Required query parameters
When you declare a default value for non-path parameters (for now, we have only seen query parameters), then it is not required.

If you don't want to add a specific value but just make it optional, set the default as None.

But when you want to make a query parameter required, you can just not declare any default value
'''

@app.get("/items/{item_id}")
def read_user_item(item_id: str, needy: str):           # Here the query parameter needy is a required query parameter of type str.
    item = {"item_id": item_id, "needy": needy}
    return item


# We can also get all the query parameters using Request object also, just like we did in django but here is a change (Its okay if you are not aware of that)

@app.get('/pages/')
def read_database(request : Request):
    query_params = dict(request.query_params)
    return {"query_params": query_params}

'''
request.query_params automatically parses repeated query parameters (e.g., ?filter=active&filter=inactive) into lists
'''