from fastapi import FastAPI, File, UploadFile
from typing import Union
from typing_extensions import Annotated
from PIL import Image
import hashlib
import os
import pathlib

from model import *
from storage import *


app = FastAPI()

DB = load_model()

BUCKET = authenticate_implicit_with_adc()

@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.post("/predict")
async def create_upload_file(image: UploadFile):
  
  # Hash file name
  filename = image.filename
  hash_filename = hashlib.md5(filename.encode()).hexdigest() + pathlib.Path(filename).suffix
  
  # Write image
  with open(hash_filename, 'wb') as img:
    content = await image.read()
    img.write(content)
    img.close()
  
  # Predict Image
  try:
    classes = predict(DB, hash_filename)
  except:
    # Error
    return {
      "error": True,
      "message": "Image is not ok"
    }

  print(classes[0])

  if classes[0]>0.5:
    pothole = False
  else:
    pothole = True
  
  url = ""
  if pothole:
    # Uload image to Storage Bucket
    print("Upload bucket")
    bucket_upload_image(BUCKET, hash_filename)
    url = "https://storage.googleapis.com/potholeimages/" + hash_filename
    print("Success url:", url)
  
  # Remove image
  os.remove(hash_filename)

  return {
    "error": False,
    "message": "Success Predict",
    "result": {
      "filename": filename,
      "pothole": pothole,
      "url": url
    }
  }

