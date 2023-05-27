from fastapi import FastAPI, File, UploadFile
from typing import Union
from typing_extensions import Annotated
from PIL import Image

from model import *

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.post("/predict/")
async def create_upload_file(file: UploadFile):
  
  # Write image
  with open('image.jpg','wb') as image:
    content = await file.read()
    image.write(content)
    image.close()
  
  classes = predict(load_model(), "image.jpg")

  print(classes[0])

  if classes[0]>0.5:
    status = "normal"
  else:
    status = "pothole"
  
  return {"filename": file.filename, "status": status, "classes": classes[0]}