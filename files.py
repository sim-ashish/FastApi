#You can define files to be uploaded by the client using File.

# install python-multipart

from typing_extensions import Annotated

from fastapi import FastAPI, File, UploadFile

from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}  # Give Size


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}   # Will give file name

'''If you declare the type of your path operation function parameter as bytes, FastAPI will read the file for you and you will receive the contents as bytes.

Keep in mind that this means that the whole contents will be stored in memory. This will work well for small files.

But there are several cases in which you might benefit from using UploadFile.'''

'''
UploadFile has the following attributes:

filename: A str with the original file name that was uploaded (e.g. myimage.jpg).
content_type: A str with the content type (MIME type / media type) (e.g. image/jpeg).
file: A SpooledTemporaryFile (a file-like object). This is the actual Python file object that you can pass directly to other functions or libraries that expect a "file-like" object.
UploadFile has the following async methods. They all call the corresponding file methods underneath (using the internal SpooledTemporaryFile).

write(data): Writes data (str or bytes) to the file.
read(size): Reads size (int) bytes/characters of the file.
seek(offset): Goes to the byte position offset (int) in the file.
E.g., await myfile.seek(0) would go to the start of the file.
This is especially useful if you run await myfile.read() once and then need to read the contents again.
close(): Closes the file.
'''

# UploadFile with Additional Metadata
# You can also use File() with UploadFile, for example, to set additional metadata:

@app.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}



# Multiple File Uploads

@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)