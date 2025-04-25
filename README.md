# FastApi

## This is my fastapi learning. I followed the fastapi official documentation to learn and implement [**FastApi**](https://fastapi.tiangolo.com/tutorial/first-steps/)

---

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

The key features are:

- Fast: Very high performance, on par with NodeJS and Go (thanks to    Starlette and Pydantic). One of the fastest Python frameworks available.
- Fast to code: Increase the speed to develop features by about 200% to 300%. *
- Fewer bugs: Reduce about 40% of human (developer) induced errors. *
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

---

### Lets's start by installing the requirements from requirements.txt

> You can do `pip install fastapi` or `pip install "fastapi[standard]"`, standard one will also install some default packages, and in simple one you have to install uvicorn(which is a server)

Create a main.py and copy paste the below code
```bash

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

```

> To install uvicorn run ` pip install uvicorn`

> To run with uvicorn `uvicorn main:app --reload`

- main is the python file name and app is the fastApi instance, you can get more idea by reading the [fastApi documentation](https://fastapi.tiangolo.com/tutorial/first-steps/)

> To run using development `fastapi dev main.py` you need to install standard version

**That's it we created our first api using only 5 lines of code**

---

### Terminologies

- #### Operation
    Here operation refers to the HTTP method.
    - .get()
    - .post()
    - .put()
    - .patch()
    - .delete()
    - .head()
    - .options()
    - .trace()

- ### path
    Here path refers to endpoint
    - In above example '/' is our endpoint which is a path

- ### Path operation decorator 
    - Decorator is @app, in our code
    - The @app.get("/") tells FastAPI that the function right below is in charge of handling requests

- ### path operation function
    The function write below the decorator is the path operation function

```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```
       
---

## Lets Start to see which module in my repo contains what!



### module1.py

contains upto, 
-  simple root
- path parameters
- path parameters with type conversion
- path operation order
- predefined value - using enum
- path inside path - like file path

### module2.py 

> $${\color{Orange}Warning}$$
>before running module2.py install python3.10+ or comment the code which i have written for 3.10+

contains upto,
- how we can write paths in a seperate file, i used class based you can use sequence also
- Query Parameters 
- Query Parameters Data Conversion
- Optional Query Parameters
- Getting all query parameters in a dictionary using the Request Object
