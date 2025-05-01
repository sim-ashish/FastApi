import uvicorn
from main import app
import sys


try:
    if sys.argv[1] == 'startserver':
        if __name__ == "__main__":
            uvicorn.run(app, port = 8000) 
except:
    print('Error : Provide startserver argument to start the server')