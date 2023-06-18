import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from script import *

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"hello": "how are you?"}


save_path = r"C:\Users\Zoheb\Documents\code\assignments\dex\files"


@app.post("/process_file")
async def process_file(file: UploadFile):
    filename = os.path.join(save_path, file.filename)
    with open(filename, "wb") as f:
        f.write(await file.read())
    extracted_data = extract_table(filename)
    return {"success": extracted_data}
